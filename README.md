Space Warrior Game is a 2D arcade-style shooter game, developed using Python and the Pygame library. The game immerses players in a fast-paced adventure where they control a spaceship to defeat enemy waves and progress through levels.
Development Details:
The game leverages the stack data structure to manage specific in-game mechanics, particularly for tracking game states, undoing actions, and handling sequences like animation frames or level transitions.
1.	Why Use Stacks?
o	Last-In-First-Out (LIFO) Property: Stacks are ideal for scenarios where the most recent action needs to be undone or revisited. For example:
	Managing states for a pause/resume feature.
	Reverting to a previous animation frame or transition state.
o	Efficient Management: Push and pop operations are O(1), making stacks efficient for real-time operations required in games.
2.	Justification of Efficiency:
o	Compared to queues or other linear structures, stacks are optimal when only the topmost element needs to be accessed or removed, reducing complexity and ensuring simplicity in code.
Key Functions Developed:
1.	Push State:
o	Adds the current game state to the stack when transitioning to a new level, scene, or menu.
2.	Pop State:
o	Retrieves the last saved state to revert to a previous screen or restore gameplay.
3.	Peek State:
o	Allows the game to view the current state without removing it, useful for handling overlays like a pause menu.
4.	Manage Animations:
o	Tracks animation frames for smoother transitions, ensuring that the most recent frame is displayed or rolled back.
5.	Undo Mechanism (Optional):
o	Enables players to revert a recent action, adding a layer of strategy and user-friendly gameplay.

Game Screenshots

![image](https://github.com/user-attachments/assets/d4ce4008-b801-4c6a-9b5d-8aa7077e7a0a)
![image](https://github.com/user-attachments/assets/8a29f3d8-0989-4db7-8c08-88c67a3ceb98)
![image](https://github.com/user-attachments/assets/3d494228-3595-42ec-a51a-0f634c8094b6)
![image](https://github.com/user-attachments/assets/fd9925d5-8a32-475d-8225-1c4a86425a5f)
![image](https://github.com/user-attachments/assets/5955cb83-0e9d-41fa-b6c2-ac79a84498a9)





