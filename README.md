# Claude Code Skills

A collection of open-source skills for [Claude Code](https://docs.anthropic.com/en/docs/claude-code).

## Available Skills

| Skill | Description |
|-------|-------------|
| [gemini-image-generator](./gemini-image-generator) | Generate images using Google Gemini |

## Installation

### Installing a Skill

1. Clone this repository or download the skill folder you want to use
2. Copy the skill folder to your Claude Code skills directory:
   - **macOS/Linux**: `~/.claude/skills/`
   - **Windows**: `%USERPROFILE%\.claude\skills\`

For example, to install the `gemini-image-generator` skill:

```bash
# Clone the repository
git clone https://github.com/mkdev-me/claude-skills.git

# Copy the skill to your Claude Code skills directory
cp -r claude-skills/gemini-image-generator ~/.claude/skills/
```

3. Follow the skill-specific setup instructions in the skill's `SKILL.md` file

### Verifying Installation

After installation, the skill should appear when you use Claude Code. You can verify by asking Claude Code to list available skills.

## Skills Documentation

### gemini-image-generator

Generate images using Google Gemini's image generation capabilities.

#### Prerequisites

- Python 3.8+
- A Google AI Studio API key

#### Setup

1. Copy the skill to your Claude Code skills directory (see above)

2. Navigate to the skill's scripts directory and set up the virtual environment:
   ```bash
   cd ~/.claude/skills/gemini-image-generator/scripts
   python3 -m venv venv
   ./venv/bin/pip install -r requirements.txt
   ```

3. Get your API key from [Google AI Studio](https://aistudio.google.com/apikey)

4. Set the environment variable:
   ```bash
   export GEMINI_API_KEY="your-api-key-here"
   ```

   For persistent configuration, add this to your shell profile (`~/.bashrc`, `~/.zshrc`, etc.):
   ```bash
   echo 'export GEMINI_API_KEY="your-api-key-here"' >> ~/.zshrc
   source ~/.zshrc
   ```

#### Usage

Once installed and configured, you can ask Claude Code to generate images:

- "Generate an image of a mountain sunset"
- "Create a logo for my app"
- "Make an image based on this reference photo"

#### Features

- **Text-to-image**: Generate images from text descriptions
- **Image-to-image**: Use reference images for style guidance
- **Multiple sizes**: Support for 1K, 2K, and 4K output resolutions

## Contributing

Contributions are welcome! To add a new skill:

1. Create a new directory with your skill name
2. Include a `SKILL.md` file with the required frontmatter:
   ```yaml
   ---
   name: your-skill-name
   description: Brief description of what your skill does
   ---
   ```
3. Add any necessary scripts in a `scripts/` subdirectory
4. Update this README with your skill information
5. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
