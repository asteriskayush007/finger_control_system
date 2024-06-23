# import cv2
# import mediapipe as mp
# import pyautogui

# # Initialize mediapipe Hands
# capture_hands = mp.solutions.hands.Hands()
# drawing_option = mp.solutions.drawing_utils
# screen_width, screen_height = pyautogui.size()
# camera = cv2.VideoCapture(0)

# scroll_speed = 10  
# click_threshold = 30  
# last_click_time = 0

# while True:
#     _, image = camera.read()
#     image_height, image_width, _ = image.shape
#     image = cv2.flip(image, 1)
#     rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#     output_hands = capture_hands.process(rgb_image)
#     all_hands = output_hands.multi_hand_landmarks

#     if all_hands:
#         for hand in all_hands:
#             drawing_option.draw_landmarks(image, hand)
#             one_hand_landmarks = hand.landmark
#             index_finger_tip = one_hand_landmarks[8]
#             thumb_tip = one_hand_landmarks[4]
            
#             # Convert coordinates to screen space
#             x1 = int(index_finger_tip.x * image_width)
#             y1 = int(index_finger_tip.y * image_height)
#             x2 = int(thumb_tip.x * image_width)
#             y2 = int(thumb_tip.y * image_height)

#             mouse_x = int(screen_width / image_width * x1)
#             mouse_y = int(screen_height / image_height * y1)
#             cv2.circle(image, (x1, y1), 10, (0, 255, 255), -1)
#             pyautogui.moveTo(mouse_x, mouse_y)

            
#             distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

            
#             if distance < click_threshold:
#                 current_time = cv2.getTickCount() / cv2.getTickFrequency()
#                 if current_time - last_click_time > 1:  
#                     pyautogui.click()
#                     last_click_time = current_time

            
#             dy = y2 - y1
#             if abs(dy) > scroll_speed:
#                 scroll_amount = dy // scroll_speed
#                 pyautogui.scroll(scroll_amount)

#     cv2.imshow("Hand Movement Video Capture", image)
#     key = cv2.waitKey(10) 
#     if key == 27:
#         break

# camera.release()
# cv2.destroyAllWindows()
