# Episode 8 – Enemy AI, Game Start Delay & End Conditions

In this episode, we add important finishing touches to the game — improving enemy behavior, controlling game flow, and handling win/lose conditions.

We enhance the enemy AI to make them chase the player more intelligently and add logic to ensure a smooth and fair start.

### 🛠️ What’s covered:
- Giving enemies a `go_after_player()` function to follow Pac-Man in real time
- Adding a short delay before the game starts
- Preventing Pac-Man from spawning too close to any enemies at the beginning or after losing a life
- Displaying a **Game Over** message when lives reach zero
- Displaying a **You Win!** message when all pellets are eaten
- Automatically closing the game window after showing the final message

By the end of this episode, we’ve turned a simple prototype into a complete, playable game — with smarter enemies, a polished flow, and proper start and end conditions.
