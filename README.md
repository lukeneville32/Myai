# OnlyFans AI Manager (OFAI)

An intelligent AI-powered manager for OnlyFans creators that handles fan interactions, sales, and entertainment. This system uses OpenAI's GPT models to respond to fans in a personalized, engaging way while helping maximize engagement and revenue.

## 🌟 Features

### 💬 AI Conversation Manager
- **Personalized Responses**: AI-powered replies that match your personality and style
- **Conversation Memory**: Maintains context across multiple interactions with each fan
- **Context-Aware**: Recognizes subscribers, tippers, and content purchasers
- **Natural Language**: Engages fans in authentic, human-like conversations

### 💰 Sales & Monetization
- **Smart Content Suggestions**: Analyzes fan messages to identify sales opportunities
- **Natural Sales Pitches**: Generates non-pushy, contextual content suggestions
- **Custom Request Handling**: Manages custom content requests professionally
- **Tip Appreciation**: Creates personalized thank-you messages based on tip amounts

### 🎮 Entertainment & Engagement
- **Flirty Games**: Generates interactive games and challenges for fan engagement
- **Story Teasers**: Creates anticipation with intriguing story snippets
- **Compliment Responses**: Graciously handles compliments while building connection
- **Daily Greetings**: Personalized greetings for different times of day
- **Conversation Starters**: Generates engaging prompts to initiate interactions

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- OpenAI API key

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/lukeneville32/Myai.git
cd Myai
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Configure environment**
```bash
cp .env.example .env
```

Edit `.env` and add your configuration:
```env
OPENAI_API_KEY=your_actual_openai_api_key_here
MODEL_NAME=Your Name
MODEL_PERSONALITY=flirty,playful,engaging
MODEL_INTERESTS=fitness,travel,photography
```

### Basic Usage

```python
from ai_manager import AIManager
from sales_manager import SalesManager
from entertainment_manager import EntertainmentManager

# Initialize the managers
ai_manager = AIManager()
sales_manager = SalesManager()
entertainment_manager = EntertainmentManager()

# Respond to a fan message
fan_id = "fan_123"
message = "Hey! How are you?"
response = ai_manager.get_response(fan_id, message)
print(response)

# Generate a sales pitch
suggestion = sales_manager.suggest_content("Do you have more photos?")
print(suggestion)

# Create entertainment content
game = entertainment_manager.generate_flirty_game()
print(game)
```

## 📖 Complete Example

Run the example script to see all features in action:

```bash
python example_usage.py
```

This demonstrates:
- Basic fan interactions
- Subscriber-specific responses
- Sales content suggestions
- Tip thank-you messages
- Entertainment features
- Conversation summaries

## 🎯 Use Cases

### Daily Fan Management
```python
# Morning greeting to all fans
greeting = entertainment_manager.generate_daily_greeting("morning")

# Respond to incoming messages
for fan_message in new_messages:
    response = ai_manager.get_response(
        fan_message.fan_id,
        fan_message.content,
        context={"is_subscriber": fan_message.is_subscriber}
    )
    send_message(fan_message.fan_id, response)
```

### Sales Optimization
```python
# Analyze message for sales opportunities
suggestion = sales_manager.suggest_content(
    fan_message,
    fan_interests=["fitness", "beach"]
)

if suggestion["confidence"] == "high":
    # Generate natural sales pitch
    pitch = sales_manager.generate_sales_response(
        fan_message,
        ContentType.PREMIUM_PHOTO
    )
```

### Engagement Boost
```python
# Send engaging content to maintain interest
story = entertainment_manager.generate_story_teaser("adventure")
game = entertainment_manager.generate_flirty_game(fan_name)
starter = entertainment_manager.generate_conversation_starter()
```

## ⚙️ Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `OPENAI_API_KEY` | Your OpenAI API key | Required |
| `MODEL_NAME` | Your display name | "Your Name" |
| `MODEL_PERSONALITY` | Comma-separated personality traits | "flirty,playful,engaging" |
| `MODEL_INTERESTS` | Comma-separated interests | "fitness,travel,photography" |
| `PREMIUM_CONTENT_PRICE` | Price for premium content | 9.99 |
| `CUSTOM_CONTENT_PRICE` | Price for custom requests | 29.99 |
| `TIP_MINIMUM` | Minimum tip amount | 5.00 |
| `MAX_RESPONSE_LENGTH` | Maximum character length | 500 |
| `RESPONSE_TEMPERATURE` | AI creativity (0.0-1.0) | 0.8 |
| `OPENAI_MODEL` | OpenAI model to use | "gpt-4" |

### Customizing Personality

The AI's personality is highly customizable through the configuration:

```python
# Edit your .env file
MODEL_PERSONALITY=flirty,playful,engaging,confident
MODEL_INTERESTS=yoga,cooking,travel,fashion,photography
```

The AI will incorporate these traits into all interactions.

## 🏗️ Architecture

```
Myai/
├── config.py                 # Configuration management
├── ai_manager.py            # Core AI conversation handler
├── sales_manager.py         # Sales and monetization features
├── entertainment_manager.py # Entertainment and engagement
├── example_usage.py         # Usage examples
├── requirements.txt         # Python dependencies
├── .env.example            # Example environment configuration
└── README.md               # This file
```

## 🔒 Security & Privacy

- **API Keys**: Never commit your `.env` file - it's in `.gitignore`
- **Data Privacy**: Conversation histories are stored in memory only
- **Safe Responses**: AI is configured with appropriate boundaries
- **No Storage**: No fan data is persisted to disk by default

## 📊 Advanced Features

### Conversation Summarization
```python
# Get a summary of conversation with a fan
summary = ai_manager.get_conversation_summary(fan_id)
```

### Context-Aware Responses
```python
# Provide context about the fan
context = {
    "is_subscriber": True,
    "has_tipped": True,
    "purchased_content": True
}
response = ai_manager.get_response(fan_id, message, context=context)
```

### Clearing Conversation History
```python
# Clear history to start fresh
ai_manager.clear_conversation(fan_id)
```

## 🛠️ Development

### Running Tests
```bash
# Install test dependencies
pip install pytest pytest-cov

# Run tests (if test files are added)
pytest tests/
```

### Contributing
Contributions are welcome! Please feel free to submit pull requests or open issues.

## 📝 License

This project is provided as-is for personal use.

## ⚠️ Disclaimer

This tool is designed to assist content creators in managing fan interactions. Users are responsible for:
- Ensuring all interactions comply with OnlyFans terms of service
- Maintaining appropriate boundaries and professional conduct
- Managing their OpenAI API usage and costs
- Reviewing AI-generated content before sending

## 🤝 Support

For issues, questions, or feature requests, please open an issue on GitHub.

## 🎉 Tips for Best Results

1. **Customize Your Personality**: Take time to set up your MODEL_PERSONALITY and MODEL_INTERESTS accurately
2. **Review Responses**: Initially review AI responses to ensure they match your style
3. **Use Context**: Provide context about fans (subscribers, tippers) for better responses
4. **Monitor Conversations**: Check conversation summaries regularly
5. **Adjust Temperature**: Lower temperature (0.5-0.7) for more consistent responses, higher (0.8-1.0) for more creativity
6. **Test Different Prompts**: Experiment with different fan messages to see how the AI responds

---

Built with ❤️ for content creators
