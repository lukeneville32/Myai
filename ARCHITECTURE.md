# Architecture Overview

## System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                     OnlyFans AI Manager                          │
│                   (onlyfans_ai.py - Main API)                    │
└───────────────────┬─────────────────────────────────────────────┘
                    │
        ┌───────────┼───────────┬──────────────┐
        │           │           │              │
        ▼           ▼           ▼              ▼
┌──────────┐ ┌─────────┐ ┌──────────┐ ┌──────────────┐
│    AI    │ │ Sales   │ │Entertainment│ │   Utils     │
│ Manager  │ │ Manager │ │  Manager   │ │  & Helpers  │
└──────────┘ └─────────┘ └──────────┘ └──────────────┘
│ai_manager│ │sales_   │ │entertainment│ │  utils.py   │
│   .py    │ │manager  │ │_manager.py │ │             │
│          │ │  .py    │ │            │ │             │
└─────┬────┘ └────┬────┘ └─────┬──────┘ └──────┬───────┘
      │           │            │                │
      │           │            │                │
      └───────────┴────────────┴────────────────┘
                               │
                               ▼
                    ┌──────────────────┐
                    │   Config Module  │
                    │   (config.py)    │
                    └──────────────────┘
                               │
                               ▼
                    ┌──────────────────┐
                    │  OpenAI API      │
                    │  (GPT-4)         │
                    └──────────────────┘
```

## Component Details

### 1. OnlyFansAIManager (Main API)
**File:** `onlyfans_ai.py`

**Purpose:** Unified interface for all AI manager features

**Key Features:**
- Fan interaction management
- Profile management
- Message routing
- Logging coordination
- Batch operations

**Main Methods:**
- `send_message()` - Handle fan messages
- `send_greeting()` - Send greetings
- `thank_for_tip()` - Thank for tips
- `create_sales_pitch()` - Generate sales pitches
- `create_flirty_game()` - Create entertainment
- `update_profile()` - Manage fan profiles

---

### 2. AIManager (Core Conversation)
**File:** `ai_manager.py`

**Purpose:** Handle AI-powered conversations

**Key Features:**
- Personality-based responses
- Conversation history management
- Context-aware messaging
- Conversation summarization

**How It Works:**
1. Maintains conversation history per fan
2. Builds system prompt from personality config
3. Includes context (subscriber, tipper, etc.)
4. Generates responses via OpenAI
5. Manages conversation memory

---

### 3. SalesManager (Monetization)
**File:** `sales_manager.py`

**Purpose:** Handle sales and monetization features

**Key Features:**
- Content suggestion from messages
- Sales pitch generation
- Tip thank-you messages
- Price management

**Content Types:**
- Premium Photo
- Premium Video
- Custom Photo
- Custom Video
- Exclusive Message

**Sales Flow:**
1. Analyze fan message
2. Identify sales opportunity
3. Determine confidence level
4. Generate natural pitch
5. Include pricing info

---

### 4. EntertainmentManager (Engagement)
**File:** `entertainment_manager.py`

**Purpose:** Create engaging content for fans

**Key Features:**
- Flirty game generation
- Story teasers
- Compliment responses
- Daily greetings
- Conversation starters

**Entertainment Types:**
- Interactive games
- Story snippets
- Personalized greetings
- Conversation prompts
- Compliment handling

---

### 5. Utils Module
**File:** `utils.py`

**Purpose:** Helper functions and utilities

**Components:**
- `FanProfile` - Fan data management
- `MessageLogger` - Message logging
- `ResponseFilter` - Response validation
- `AnalyticsSummary` - Analytics helpers

---

### 6. Config Module
**File:** `config.py`

**Purpose:** Configuration management

**Configuration:**
- API keys
- Model settings
- Personality traits
- Pricing info
- Response settings

---

## Data Flow

### Message Flow

```
Fan Message
    │
    ▼
┌─────────────────────┐
│ OnlyFansAIManager   │
│  - Validate input   │
│  - Get fan profile  │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│    AIManager        │
│  - Load history     │
│  - Build context    │
│  - Generate prompt  │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│    OpenAI API       │
│  - Process prompt   │
│  - Generate text    │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  Response Filter    │
│  - Sanitize text    │
│  - Check length     │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  Sales Analysis     │
│  - Detect opps      │
│  - Add suggestions  │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   Message Logger    │
│  - Log interaction  │
└──────────┬──────────┘
           │
           ▼
    Return Response
```

### Sales Flow

```
Fan Message
    │
    ▼
┌─────────────────────┐
│  SalesManager       │
│  - Analyze content  │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   OpenAI API        │
│  - Detect intent    │
│  - Classify type    │
└──────────┬──────────┘
           │
           ▼
     ┌────┴────┐
     │         │
High Confidence   Low Confidence
     │              │
     ▼              ▼
Generate Pitch   Regular Response
```

## File Dependencies

```
onlyfans_ai.py
├── ai_manager.py
│   └── config.py
├── sales_manager.py
│   └── config.py
├── entertainment_manager.py
│   └── config.py
└── utils.py

interactive_demo.py
└── onlyfans_ai.py

simple_example.py
└── onlyfans_ai.py

example_usage.py
├── ai_manager.py
├── sales_manager.py
└── entertainment_manager.py
```

## Configuration Flow

```
.env file
    │
    ▼
┌─────────────────────┐
│   Config Class      │
│  - Load env vars    │
│  - Validate values  │
│  - Provide defaults │
└──────────┬──────────┘
           │
           └─────────────┬─────────────┬─────────────┐
                         │             │             │
                         ▼             ▼             ▼
                  AIManager    SalesManager  EntertainmentManager
```

## Storage and Persistence

### Current Implementation (In-Memory)
```
OnlyFansAIManager
├── fan_profiles: Dict[str, FanProfile]
│   └── Stored in memory
└── ai_manager.conversation_history: Dict[str, List]
    └── Stored in memory

MessageLogger
└── messages.log
    └── Appended to file
```

### Future Implementation (Optional)
```
Database Layer (Not Implemented)
├── Fan Profiles
├── Conversation History
├── Message Logs
├── Analytics Data
└── Sales History
```

## Error Handling

```
User Input
    │
    ▼
┌─────────────────────┐
│  Input Validation   │
└──────────┬──────────┘
           │
      ┌────┴────┐
   Valid?    Invalid
      │          │
      ▼          ▼
   Process   Return Error
      │
      ▼
┌─────────────────────┐
│  API Call           │
└──────────┬──────────┘
           │
      ┌────┴────┐
  Success?   Fail
      │         │
      ▼         ▼
   Return    Fallback
   Result    Response
```

## Key Design Decisions

### 1. Modular Architecture
- Separate concerns (conversation, sales, entertainment)
- Easy to extend and maintain
- Independent testing of components

### 2. Unified API
- Single entry point (OnlyFansAIManager)
- Simplified usage
- Consistent interface

### 3. Configuration-Driven
- Environment-based config
- No hardcoded values
- Easy customization

### 4. In-Memory Storage
- Fast access
- No database setup required
- Easy migration to persistent storage later

### 5. OpenAI Integration
- Leverages GPT-4 capabilities
- Natural language understanding
- Context-aware responses

## Scaling Considerations

### Current Limitations
- In-memory storage (not persistent)
- Single-threaded processing
- No caching layer
- Direct API calls

### Future Scaling Options
1. **Add Database Layer**
   - PostgreSQL for structured data
   - Redis for caching
   - MongoDB for conversation logs

2. **Add Queue System**
   - RabbitMQ or Redis Queue
   - Background job processing
   - Scheduled messages

3. **Add Caching**
   - Response caching
   - Profile caching
   - API response caching

4. **Add Rate Limiting**
   - Per-fan limits
   - API call limits
   - Cost management

5. **Add Analytics**
   - Engagement metrics
   - Revenue tracking
   - Performance monitoring

---

## Getting Started with Development

1. **Set up environment**
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Configure settings**
   ```bash
   cp .env.example .env
   # Edit .env with your settings
   ```

3. **Run examples**
   ```bash
   python interactive_demo.py
   ```

4. **Modify components**
   - Edit personality in `config.py`
   - Customize prompts in manager files
   - Add new features in respective modules

---

For more information, see:
- README.md - Overview and features
- QUICKSTART.md - Getting started guide
- API_REFERENCE.md - Complete API documentation
