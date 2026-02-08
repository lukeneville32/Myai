# Quick Start Guide

Get your OnlyFans AI Manager up and running in 5 minutes!

## Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

## Step 2: Set Up Your API Key

1. Copy the example environment file:
```bash
cp .env.example .env
```

2. Get your OpenAI API key:
   - Go to https://platform.openai.com/api-keys
   - Create a new API key
   - Copy it

3. Edit `.env` file and add your key:
```env
OPENAI_API_KEY=sk-your-actual-key-here
MODEL_NAME=YourName
MODEL_PERSONALITY=flirty,playful,engaging,confident
MODEL_INTERESTS=fitness,travel,photography,fashion
```

## Step 3: Try It Out!

### Option A: Interactive Demo (Recommended for first time)
```bash
python interactive_demo.py
```

This launches an interactive menu where you can:
- Send messages as fans and see AI responses
- Generate sales pitches
- Create entertainment content
- Test all features

### Option B: Run Examples
```bash
python simple_example.py
```

This runs through all features automatically with example scenarios.

### Option C: Use the API in Your Code

```python
from onlyfans_ai import OnlyFansAIManager
from sales_manager import ContentType

# Initialize
ai = OnlyFansAIManager()

# Update fan profile
ai.update_profile(
    fan_id="fan_123",
    name="John",
    is_subscriber=True,
    interests=["fitness"]
)

# Get AI response to fan message
result = ai.send_message(
    fan_id="fan_123",
    message="Hey! How are you?"
)

print(result['response'])

# Thank for tip
thanks = ai.thank_for_tip(
    fan_id="fan_123",
    tip_amount=25.00,
    fan_name="John"
)

print(thanks)

# Create entertainment
game = ai.create_flirty_game(fan_id="fan_123", fan_name="John")
print(game)
```

## Step 4: Customize Your AI

Edit your `.env` file to customize the AI's personality:

```env
# Make the AI more professional
MODEL_PERSONALITY=friendly,professional,warm,engaging

# Focus on specific interests
MODEL_INTERESTS=yoga,cooking,travel,art,music

# Adjust response style
RESPONSE_TEMPERATURE=0.7  # Lower = more consistent, Higher = more creative
MAX_RESPONSE_LENGTH=300   # Shorter responses
```

## Common Use Cases

### Daily Fan Engagement
```python
ai = OnlyFansAIManager()

# Send morning greeting
greeting = ai.send_greeting("fan_123", custom_time="morning")

# Create conversation starter
starter = ai.create_conversation_starter("fan_123")
```

### Handling Sales Inquiries
```python
# Fan asks about content
result = ai.send_message(
    fan_id="fan_123",
    message="Do you have any beach photos?"
)

# Check if sales opportunity was detected
if "sales_opportunity" in result:
    print("Sales opportunity detected!")
    print(result['sales_opportunity'])
```

### Managing Tips
```python
# Thank fan for tip with personalized message
thanks = ai.thank_for_tip(
    fan_id="fan_123",
    tip_amount=50.00,
    fan_name="Mike"
)
```

### Entertainment and Engagement
```python
# Create a flirty game
game = ai.create_flirty_game(fan_id="fan_123", fan_name="Sarah")

# Create story teaser
story = ai.create_story_teaser(fan_id="fan_123", theme="adventure")

# Respond to compliments
response = ai.respond_to_compliment(
    fan_id="fan_123",
    compliment="You look amazing!"
)
```

## Tips for Best Results

1. **Customize Your Personality**: Spend time getting your personality traits right
2. **Update Fan Profiles**: Keep fan profiles updated with preferences
3. **Review Initial Responses**: Check early AI responses to ensure they match your style
4. **Use Context**: Provide subscriber/tipper info for better responses
5. **Monitor Sales Suggestions**: The AI will detect sales opportunities automatically

## Troubleshooting

### "OPENAI_API_KEY must be set"
- Make sure you created `.env` file (not just `.env.example`)
- Ensure your API key is valid and active
- Check that there are no quotes around the key in `.env`

### Responses don't match my style
- Adjust `MODEL_PERSONALITY` in `.env`
- Change `RESPONSE_TEMPERATURE` (0.7 = consistent, 0.9 = creative)
- Review your `MODEL_INTERESTS` - they influence the responses

### Responses are too long/short
- Adjust `MAX_RESPONSE_LENGTH` in `.env`

### Getting OpenAI API errors
- Check your API key is valid
- Ensure you have credits in your OpenAI account
- Try using `gpt-3.5-turbo` instead of `gpt-4` (cheaper, faster)

```env
OPENAI_MODEL=gpt-3.5-turbo
```

## Next Steps

1. Integrate with your OnlyFans messaging system
2. Set up automated responses for common questions
3. Use analytics to track engagement
4. Customize sales pitches for your content style

## Need Help?

- Check the full README.md for detailed documentation
- Review example_usage.py for more code examples
- Run interactive_demo.py to test features interactively

---

Happy fan engaging! 🎉
