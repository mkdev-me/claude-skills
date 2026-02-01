#!/bin/sh
''''exec "`dirname $0`/venv/bin/python3" "$0" "$@" #'''
import argparse
import os
import sys
from google import genai
from google.genai import types
from PIL import Image


def main():
    parser = argparse.ArgumentParser(
        description="Generate images using Google Gemini.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --prompt "A cat in space" --output cat.png
  %(prog)s --prompt "Same style but blue" --reference input.png --output blue.png
  %(prog)s --prompt "Abstract art" --output art.png --size 2K
        """
    )
    parser.add_argument(
        "--prompt",
        required=True,
        help="Text prompt describing the image to generate"
    )
    parser.add_argument(
        "--output",
        required=True,
        help="Output file path for the generated image"
    )
    parser.add_argument(
        "--reference",
        action="append",
        help="Optional reference image path(s) for style/content guidance. Can be specified multiple times."
    )
    parser.add_argument(
        "--size",
        default="4K",
        choices=["1K", "2K", "4K"],
        help="Output image size (default: 4K)"
    )
    args = parser.parse_args()

    # Get API key from environment
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Error: GOOGLE_API_KEY environment variable not set.", file=sys.stderr)
        print("Set it with: export GOOGLE_API_KEY='your-api-key'", file=sys.stderr)
        sys.exit(1)

    client = genai.Client(api_key=api_key)

    # Build content list
    contents = [args.prompt]

    # Add reference images if provided
    if args.reference:
        for ref_path in args.reference:
            try:
                reference_image = Image.open(ref_path)
                contents.append(reference_image)
                print(f"Using reference image: {ref_path}")
            except FileNotFoundError:
                print(f"Error: Reference image '{ref_path}' not found.", file=sys.stderr)
                sys.exit(1)
            except Exception as e:
                print(f"Error loading reference image: {e}", file=sys.stderr)
                sys.exit(1)

    # Create output directory if it doesn't exist
    output_dir = os.path.dirname(args.output)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created output directory: {output_dir}")

    print(f"Generating image with size: {args.size}...")

    try:
        response = client.models.generate_content(
            model="gemini-3-pro-image-preview",
            contents=contents,
            config=types.GenerateContentConfig(
                image_config=types.ImageConfig(
                    image_size=args.size,
                )
            )
        )
    except Exception as e:
        print(f"Error generating image: {e}", file=sys.stderr)
        sys.exit(1)

    # Process response
    image_saved = False
    for part in response.parts:
        if part.text is not None:
            print(f"Model response: {part.text}")
        elif part.inline_data is not None:
            generated_image = part.as_image()
            generated_image.save(args.output)
            print(f"Image saved to: {args.output}")
            image_saved = True

    if not image_saved:
        print("Warning: No image was generated in the response.", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
