# API Reference

Complete API documentation for the OnlyFans AI Manager.

## Table of Contents
- [OnlyFansAIManager](#onlyfansaimanager)
- [AIManager](#aimanager)
- [SalesManager](#salesmanager)
- [EntertainmentManager](#entertainmentmanager)
- [Utils](#utils)

---

## OnlyFansAIManager

The main unified interface for all AI manager features.

### Initialization

```python
from onlyfans_ai import OnlyFansAIManager

ai = OnlyFansAIManager(enable_logging=True)
```

**Parameters:**
- `enable_logging` (bool): Whether to log messages to file. Default: `True`

### Methods

#### send_message()

Send a message to a fan and get AI response.

```python
result = ai.send_message(
    fan_id="fan_123",
    message="Hey! How are you?",
    auto_analyze_sales=True
)
```

**Parameters:**
- `fan_id` (str): Unique identifier for the fan
- `message` (str): The fan's message
- `auto_analyze_sales` (bool): Automatically analyze for sales opportunities. Default: `True`

**Returns:**
- `dict`: Dictionary with keys:
  - `response` (str): AI-generated response
  - `fan_id` (str): The fan's ID
  - `sales_opportunity` (dict, optional): Sales analysis if opportunity detected

**Example:**
```python
result = ai.send_message("fan_123", "Do you have more photos?")
print(result['response'])
if 'sales_opportunity' in result:
    print(f"Sales opportunity: {result['sales_opportunity']['content_type']}")
```

---

#### send_greeting()

Send a personalized greeting to a fan.

```python
greeting = ai.send_greeting(
    fan_id="fan_123",
    custom_time="morning"
)
```

**Parameters:**
- `fan_id` (str): Unique identifier for the fan
- `custom_time` (str, optional): Time of day - "morning", "afternoon", "evening", or "night"

**Returns:**
- `str`: Greeting message

---

#### thank_for_tip()

Generate a personalized thank you message for a tip.

```python
thanks = ai.thank_for_tip(
    fan_id="fan_123",
    tip_amount=25.00,
    fan_name="John"
)
```

**Parameters:**
- `fan_id` (str): Unique identifier for the fan
- `tip_amount` (float): Amount of the tip in dollars
- `fan_name` (str, optional): Fan's name for personalization

**Returns:**
- `str`: Thank you message

---

#### create_sales_pitch()

Create a natural sales pitch for specific content.

```python
from sales_manager import ContentType

pitch = ai.create_sales_pitch(
    fan_id="fan_123",
    fan_message="I'd love to see more content",
    content_type=ContentType.PREMIUM_VIDEO,
    custom_details="Behind the scenes workout"
)
```

**Parameters:**
- `fan_id` (str): Unique identifier for the fan
- `fan_message` (str): The fan's original message
- `content_type` (ContentType): Type of content to pitch
- `custom_details` (str, optional): Custom details about the content

**Returns:**
- `str`: Sales pitch message

**Content Types:**
- `ContentType.PREMIUM_PHOTO`
- `ContentType.PREMIUM_VIDEO`
- `ContentType.CUSTOM_PHOTO`
- `ContentType.CUSTOM_VIDEO`
- `ContentType.EXCLUSIVE_MESSAGE`

---

#### create_flirty_game()

Create an engaging game for fan interaction.

```python
game = ai.create_flirty_game(
    fan_id="fan_123",
    fan_name="Sarah"
)
```

**Parameters:**
- `fan_id` (str): Unique identifier for the fan
- `fan_name` (str, optional): Fan's name for personalization

**Returns:**
- `str`: Game message

---

#### create_story_teaser()

Create an intriguing story teaser.

```python
story = ai.create_story_teaser(
    fan_id="fan_123",
    theme="beach adventure"
)
```

**Parameters:**
- `fan_id` (str): Unique identifier for the fan
- `theme` (str, optional): Theme for the story

**Returns:**
- `str`: Story teaser message

---

#### respond_to_compliment()

Generate a gracious response to a compliment.

```python
response = ai.respond_to_compliment(
    fan_id="fan_123",
    compliment="You look amazing!"
)
```

**Parameters:**
- `fan_id` (str): Unique identifier for the fan
- `compliment` (str): The compliment received

**Returns:**
- `str`: Response message

---

#### create_conversation_starter()

Generate an engaging conversation starter.

```python
starter = ai.create_conversation_starter(fan_id="fan_123")
```

**Parameters:**
- `fan_id` (str): Unique identifier for the fan

**Returns:**
- `str`: Conversation starter message

---

#### update_profile()

Update a fan's profile information.

```python
ai.update_profile(
    fan_id="fan_123",
    name="John",
    is_subscriber=True,
    subscription_tier="VIP",
    interests=["fitness", "travel"],
    notes="Regular tipper, loves workout content"
)
```

**Parameters:**
- `fan_id` (str): Unique identifier for the fan
- `name` (str, optional): Fan's name
- `is_subscriber` (bool, optional): Whether they're a subscriber
- `subscription_tier` (str, optional): Subscription tier
- `interests` (list, optional): List of interests
- `notes` (str, optional): Notes about the fan

---

#### get_profile()

Get a fan's profile information.

```python
profile = ai.get_profile("fan_123")
print(f"Name: {profile.name}")
print(f"Subscriber: {profile.is_subscriber}")
print(f"Total Tips: ${profile.total_tips}")
```

**Parameters:**
- `fan_id` (str): Unique identifier for the fan

**Returns:**
- `FanProfile` or `None`: Fan profile object if exists

---

#### get_conversation_summary()

Get a summary of conversation with a fan.

```python
summary = ai.get_conversation_summary("fan_123")
```

**Parameters:**
- `fan_id` (str): Unique identifier for the fan

**Returns:**
- `str` or `None`: Conversation summary if history exists

---

#### clear_conversation()

Clear conversation history for a fan.

```python
ai.clear_conversation("fan_123")
```

**Parameters:**
- `fan_id` (str): Unique identifier for the fan

---

#### broadcast_message()

Send a message to multiple fans at once.

```python
results = ai.broadcast_message(
    fan_ids=["fan_1", "fan_2", "fan_3"],
    message_type="greeting"
)
```

**Parameters:**
- `fan_ids` (list): List of fan IDs
- `message_type` (str): Type of message - "greeting", "starter", or "game"

**Returns:**
- `dict`: Dictionary mapping fan_id to message

---

## Configuration

All configuration is managed through environment variables in `.env` file.

### Environment Variables

```env
# Required
OPENAI_API_KEY=your_api_key_here

# Model Settings
MODEL_NAME=Your Name
MODEL_PERSONALITY=flirty,playful,engaging
MODEL_INTERESTS=fitness,travel,photography

# Sales Settings
PREMIUM_CONTENT_PRICE=9.99
CUSTOM_CONTENT_PRICE=29.99
TIP_MINIMUM=5.00

# Response Settings
MAX_RESPONSE_LENGTH=500
RESPONSE_TEMPERATURE=0.8
OPENAI_MODEL=gpt-4
```

### Config Class

```python
from config import Config

# Access configuration
print(Config.MODEL_NAME)
print(Config.RESPONSE_TEMPERATURE)

# Validate configuration
Config.validate()  # Raises ValueError if invalid
```

---

## FanProfile

Data class for storing fan profile information.

### Attributes

- `fan_id` (str): Unique identifier
- `name` (str): Fan's name
- `is_subscriber` (bool): Whether they're a subscriber
- `subscription_tier` (str): Subscription tier
- `total_tips` (float): Total amount tipped
- `content_purchased` (int): Number of content purchases
- `last_interaction` (datetime): Last interaction timestamp
- `interests` (list): List of interests
- `notes` (str): Notes about the fan

### Methods

```python
# Convert to context dict for AI
context = profile.to_context()

# Convert to dictionary
data = profile.to_dict()

# Create from dictionary
profile = FanProfile.from_dict(data)
```

---

## Complete Example

```python
from onlyfans_ai import OnlyFansAIManager
from sales_manager import ContentType

# Initialize
ai = OnlyFansAIManager()

# Set up fan profile
ai.update_profile(
    fan_id="fan_john",
    name="John",
    is_subscriber=True,
    interests=["fitness", "travel"]
)

# Handle incoming message
result = ai.send_message(
    fan_id="fan_john",
    message="Hey! Do you have any workout videos?"
)

print(f"Response: {result['response']}")

# If sales opportunity detected
if 'sales_opportunity' in result:
    pitch = ai.create_sales_pitch(
        fan_id="fan_john",
        fan_message="workout videos",
        content_type=ContentType.PREMIUM_VIDEO
    )
    print(f"Sales pitch: {pitch}")

# Fan tips
thanks = ai.thank_for_tip(
    fan_id="fan_john",
    tip_amount=25.00,
    fan_name="John"
)
print(f"Thanks: {thanks}")

# Create engagement content
game = ai.create_flirty_game(fan_id="fan_john", fan_name="John")
story = ai.create_story_teaser(fan_id="fan_john", theme="adventure")

# Get conversation summary
summary = ai.get_conversation_summary("fan_john")
print(f"Summary: {summary}")

# Check profile
profile = ai.get_profile("fan_john")
print(f"Total tips: ${profile.total_tips}")
```

---

## Error Handling

```python
try:
    ai = OnlyFansAIManager()
except ValueError as e:
    print(f"Configuration error: {e}")
    # Handle missing API key or invalid config

try:
    result = ai.send_message("fan_123", "Hello")
except Exception as e:
    print(f"Error generating response: {e}")
    # Handle API errors or other issues
```

---

## Best Practices

1. **Always update fan profiles** with subscriber status and interests
2. **Use context** when sending messages for better responses
3. **Handle sales opportunities** gracefully - don't spam
4. **Log interactions** for analytics and improvement
5. **Review AI responses** initially to ensure they match your style
6. **Clear conversations** when starting fresh or after long gaps
7. **Customize configuration** to match your personality and pricing

---

For more examples, see:
- `simple_example.py` - Basic usage examples
- `example_usage.py` - Comprehensive feature demo
- `interactive_demo.py` - Interactive testing
