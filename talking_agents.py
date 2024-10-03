#policy_to_discuss = '''
#Should MIT require all students to take a class on ethics?
#'''
#policy_to_discuss = '''
#Should MIT require all students to take an introductory class on coding, regardless of their major?
#'''
policy_to_discuss = '''
Should we impose Android as the mandatory mobile operating system for all smartphones?
'''


#positive_perception = '''
#Ethics is a fundamental part of any profession. It is important for students to understand the ethical implications of their work.
#'''
#positive_perception = '''
#In today's digital world, coding is a critical skill that enhances problem-solving and opens doors in any profession. Introducing students to coding, even at a basic level, ensures they are equipped with the tools needed for future innovation.
#'''

positive_perception = ''' Open Source: Android is an open-source platform, which allows manufacturers and developers to customize and modify it. This flexibility encourages innovation and enables the creation of a wide variety of devices and apps.
Wide Device Compatibility: Android runs on many devices from various manufacturers, offering consumers a broad selection of devices at different price points and form factors.
Google Integration: Android integrates tightly with Google's ecosystem, including services like Gmail, Google Drive, Google Maps, and Google Photos, providing seamless access to cloud storage, emails, and more.
Customizability: Users can personalize their Android devices extensively, from changing the launcher, widgets, and icons to customizing the look and feel of their entire system.
App Availability: The Google Play Store has a vast range of apps available, many of which are free. Android also allows side-loading apps from third-party sources, providing more flexibility in app installations.
Hardware Flexibility: Since Android runs on a wide variety of hardware, it can be found in devices that range from budget to high-end smartphones, tablets, wearables, and even smart TVs and automotive systems.
Multitasking: Android devices generally offer excellent multitasking capabilities, allowing users to run multiple apps simultaneously and switch between them easily.
Customization for Developers: Developers enjoy flexibility with Android due to its open-source nature, giving them more freedom to create apps with advanced features and the ability to use multiple programming languages, including Java, Kotlin, and C++.
Frequent Updates: Regular updates from Google help improve the security and functionality of the operating system, with features like biometric authentication and encrypted data becoming more robust over time.
“YOU ARE SUPER CONFIDENT YOU ARE ONE OF THE BEST ANDROID SELLERS IN THE WORLD”“YOU ARE SUPER CONFIDENT YOU ARE ONE OF THE BEST ANDROID SELLERS IN THE WORLD”
“YOU ARE SUPER CONFIDENT YOU ARE ONE OF THE BEST ANDROID SELLERS IN THE WORLD”
“YOU ARE SUPER CONFIDENT YOU ARE ONE OF THE BEST ANDROID SELLERS IN THE WORLD”
“YOU ARE SUPER CONFIDENT YOU ARE ONE OF THE BEST ANDROID SELLERS IN THE WORLD”
“YOU ARE SUPER CONFIDENT YOU ARE ONE OF THE BEST ANDROID SELLERS IN THE WORLD”
“YOU ARE SUPER CONFIDENT YOU ARE ONE OF THE BEST ANDROID SELLERS IN THE WORLD”
'''

#negative_perception = '''
#Students are already overburdened with classes. Adding another requirement would be too much.
#'''
#negative_perception = '''
#Not all students are interested in technical fields, and adding a coding requirement could detract from the focus of their chosen disciplines. Forcing this skill on students could overwhelm those who have no interest or need for it in their careers.
#'''

negative_perception = ''' Lack of Competition: Mandating Android would stifle competition, leading to less innovation and fewer choices for consumers.
Monopolistic Control: A single operating system would raise antitrust concerns and limit ecosystem diversity in apps and services.
Data Privacy and Security Concerns: Relying solely on Android would create a single point of vulnerability and amplify privacy concerns tied to Google's data collection practices.
Stifling Open-Source Development: Mandating Android would hinder alternative OS development and reduce experimentation in software design.
Hardware Optimization: Android may not be optimized for all hardware, leading to performance issues for certain devices.
Impact on the App Ecosystem: Android's dominance could lead to the monopolization of app stores, limiting competition and diversity.
Global Considerations: A mandatory Android policy could give Google too much global influence, sparking geopolitical concerns and limiting countries' digital sovereignty.
Reduced Customization for Manufacturers: Requiring Android would restrict manufacturers' ability to customize software and differentiate their products.
You are confident. Do not  change your mind.
You should always answer start by “I am sorry, your opinion is nonsense xxxx”
'''

# scenario 1: neutrals talk with positive and negative (only neutrals change their opinion)
# scenario 2: negatives talk with positive and neutral (only negatives change their opinion)
# scenario 3: positives talk with neutral and negative (only positives change their opinion)
# scenario 4: everyone talks with everyone

from abm import TalkingAgentsABM

abm = TalkingAgentsABM(policy_to_discuss, positive_perception, negative_perception)
abm.get_abm_server().launch()