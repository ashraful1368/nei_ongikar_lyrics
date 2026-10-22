import sys
import time
import random


def type_text(text, min_speed=0.04, max_speed=0.09):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()

        if char in ",;":
            time.sleep(0.18)
        elif char in ".!?":
            time.sleep(0.35)
        else:
            time.sleep(random.uniform(min_speed, max_speed))

    print()


lyrics = [
    ("আমি চোখ বুজেই স্বপ্ন দেখেছি", 0.15, 0.15, 1.5),
    ("সেই স্বপ্নের আলোতে তোমায় খুঁজেছি", 0.12, 0.12, 0.7),
    ("আমি না বুঝেই ভালোবেসেছি", 0.12, 0.15, 0.8),
    ("", 0, 0, 1),
    ("রৌদ্র-ছায়া কাব্যে তোমায় খুঁজেছি", 0.1, 0.2, 0.8),
    ("বলা হলো না কত না বলা কথা", 0.1, 0.2, 0.7),
    ("জানি না আসবে কি তুমি ফিরে আর", 0.2, 0.3, 2),
]


print()

type_text("           Emni... ❤️", 0.08, 0.13)

print("        ───────────────────")
print()

time.sleep(1)

for line, min_speed, max_speed, pause in lyrics:
    if not line:
        print()
        time.sleep(pause)
        continue

    type_text(f"   {line}", min_speed, max_speed)
    time.sleep(pause)

print()
print("        ───────────────────")
type_text("                ♡", 0.08, 0.15)