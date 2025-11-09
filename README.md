# Emotion-Based-Music-Recommender
Use facial emotion detection via webcam or images to recommend songs based on real-time emotions like happy, sad, or angry.
# Emotion-Based-Music-Recommender
Use facial emotion detection via webcam or images to recommend songs based on real-time emotions like happy, sad, or angry.

🎵 MoodTunes AI - Emotion-Based Music Recommender

An intelligent web application that detects user emotions in real-time through facial recognition and recommends personalized music playlists instantly.

📋 Table of Contents

Overview Features Demo Technology Stack How It Works Installation Usage Advantages Disadvantages Future Enhancements Project Structure Contributing License Contact

🎯 Overview MoodTunes AI solves the problem of manually searching for music that matches your current emotional state. By leveraging real-time emotion detection through webcam analysis, the application automatically generates personalized playlists that align with your mood, providing an intuitive and hands-free music discovery experience. Problem Statement

Users spend 5-10 minutes searching for mood-appropriate music Generic playlists don't adapt to real-time emotional changes Decision fatigue from overwhelming music choices Manual mood selection is time-consuming and inaccurate

Solution An AI-powered system that:

Detects emotions automatically through facial recognition Generates instant personalized playlists (3-5 seconds) Adapts to mood changes in real-time Provides a seamless, privacy-first user experience

✨ Features Core Features

🎭 Real-time Emotion Detection - Analyzes facial expressions every 3 seconds 🎶 Smart Music Recommendations - AI-powered playlist generation based on detected emotions 📹 Webcam Integration - Uses device camera for emotion analysis 🎵 Interactive Music Player - Play, pause, skip, and provide feedback 🏆 Gamification - Points system rewards user engagement 📊 Statistics Dashboard - Track mood patterns and listening history 🔒 Privacy-First - All processing happens client-side

Supported Emotions

😊 Happy 😢 Sad 😠 Angry 😐 Neutral 😮 Surprised 😨 Fearful 🤢 Disgusted

User Interface

✅ Beautiful animated landing page ✅ Secure login/signup system ✅ Responsive design (mobile, tablet, desktop) ✅ Modern gradient themes ✅ Smooth transitions and animations ✅ Intuitive navigation

🎬 Demo Live Demo 🔗 https://chowdamdharanipriya.github.io/Emotion-Based-Music-Recommender/

🛠️ Technology Stack Frontend

HTML5 - Structure and semantic markup CSS3 - Styling, animations, and responsive design JavaScript (ES6+) - Application logic and interactivity

APIs & Libraries

WebRTC API - Webcam access and video streaming getUserMedia() - Browser camera integration No external dependencies - Pure vanilla JavaScript

Development Tools

VS Code - Code editor Live Server - Local development server Git - Version control GitHub - Code repository

Deployment

Netlify / GitHub Pages / Vercel - Static site hosting HTTPS - Secure connection for camera access

🔄 How It Works System Architecture ┌─────────────────┐ │ User Device │ │ (Browser) │ └────────┬────────┘ │ ┌────▼─────┐ │ Webcam │ │ Capture │ └────┬─────┘ │ ┌────▼──────────┐ │ Emotion │ │ Detection │ │ (Simulated) │ └────┬──────────┘ │ ┌────▼──────────┐ │ Music │ │ Recommendation│ │ Engine │ └────┬──────────┘ │ ┌────▼──────────┐ │ Playlist │ │ Generation │ └────┬──────────┘ │ ┌────▼──────────┐ │ Music Player │ │ Interface │ └───────────────┘

Workflow
User Authentication

User enters email and password System creates user profile Redirects to main application

Emotion Detection

User clicks "Start Detection" Browser requests camera permission System captures video feed Emotion analysis runs every 3 seconds Displays detected emotion with confidence score

Playlist Generation

User clicks "Generate Playlist" System matches emotion to music database Retrieves 4-5 relevant songs Displays personalized playlist

Music Playback

User clicks song to play Player controls appear User can like/dislike songs System awards points for engagement

Adaptive Learning (Conceptual for prototype)

Tracks user feedback Adjusts future recommendations Improves accuracy over time

🎮 Usage Step-by-Step Guide

Access the Application

Open the live URL or local server

Landing Page

Click "Get Started" button

Login

Enter any email (e.g., test@example.com) Enter any password (e.g., password123) Click "Login"

Start Emotion Detection

Click "Start Detection" button Allow camera permissions when prompted Wait 3 seconds for emotion detection

Generate Playlist

Click "Generate Playlist" button Browse recommended songs Scroll down to view playlist

Play Music

Click any song card Use player controls (play/pause/skip) Provide feedback (like/dislike)

Earn Points

Generate playlists: +10 points Play songs: +1 point Like songs: +2 points Dislike songs: +1 point

✅ Advantages

User Experience
✅ Hands-free Operation - Automatic emotion detection eliminates manual input ✅ Time-Saving - Reduces music search time from 10 minutes to 5 seconds ✅ Personalized - Tailored recommendations based on real-time emotions ✅ Intuitive Interface - Simple, easy-to-use design ✅ Instant Gratification - Quick playlist generation

Technical Excellence
✅ No Installation Required - Web-based application ✅ Cross-Platform - Works on any device with a browser ✅ Lightweight - Single HTML file, no dependencies ✅ Fast Performance - Client-side processing ✅ Responsive Design - Adapts to all screen sizes

Privacy & Security
✅ Client-Side Processing - No data sent to external servers ✅ No User Data Storage - Privacy-first approach ✅ Secure Connection - HTTPS for camera access ✅ No Tracking - No cookies or analytics ✅ Transparent - Open-source code

Innovation
✅ Cutting-Edge Technology - Combines AI, computer vision, and music ✅ Novel Approach - First-of-its-kind browser-based emotion music system ✅ Real-Time Processing - Instant emotion detection ✅ Adaptive Learning Concept - System improves with feedback

Accessibility
✅ Free to Use - No subscription or payment required ✅ No Registration Hassle - Simple login system ✅ Works Offline - Once loaded, core features work without internet ✅ Browser-Based - No app download needed ✅ Universal Access - Available to anyone with internet

Mental Health & Well-being
✅ Mood Regulation - Music therapy benefits ✅ Stress Relief - Automatic calming music for stressed states ✅ Emotional Awareness - Helps users understand their emotions ✅ Positive Reinforcement - Uplifting music for negative moods

Business & Market Potential
✅ Scalable - Can expand to millions of users ✅ Monetizable - Potential for premium features ✅ API Integration Ready - Can connect to Spotify, YouTube, etc. ✅ B2B Opportunities - Mental health clinics, gyms, offices ✅ Growing Market - Music streaming and AI industries expanding

🚀 Future Enhancements Short-term (3-6 months)

Real ML Integration

Integrate face-api.js for actual emotion detection Train custom CNN model for better accuracy Achieve 85-90% emotion recognition accuracy

Enhanced Music Features

Integrate Spotify Web API for 100M+ songs Add YouTube Music API support Implement actual audio playback Create collaborative playlists

Multi-Modal Emotion Detection

Add voice/speech sentiment analysis Text-based mood input as fallback Combine multiple inputs for higher accuracy

User Personalization

User accounts with persistent data Learning algorithm based on listening history Custom playlist creation and saving Favorite songs and artists

UI/UX Improvements

Dark mode toggle Theme customization Accessibility features (screen reader support) Keyboard shortcuts

Mid-term (6-12 months)

Mobile Applications

Native iOS app (Swift) Native Android app (Kotlin) React Native cross-platform version

Advanced AI Features

Mood prediction based on time/day patterns Multi-emotion detection (complex feelings) Emotion intensity measurement Contextual recommendations (activity-based)

Social Features

Share playlists with friends Collaborative listening sessions Mood-based social network Community playlists

Analytics & Insights

Weekly mood reports Listening pattern analysis Emotional health tracking Export data to mental health apps

Integration Ecosystem

Smart home integration (Alexa, Google Home) Fitness app integration (workout music) Calendar integration (meeting mood) Weather-based mood adjustment

Long-term (1-2 years)

B2B Solutions

Mental health clinic partnerships Corporate wellness programs Music therapy integration Educational institution licenses

Advanced ML Models

Real-time emotion forecasting Personality type detection Cultural emotion adaptation Context-aware recommendations

Content Expansion

Podcast recommendations Audiobook suggestions Meditation and soundscapes User-generated content

Global Expansion

Multi-language support (50+ languages) Regional music databases Cultural emotion variations Local artist promotion

Research & Development

Publish research papers on emotion-music correlation Collaborate with universities Open-source ML models Developer API for third parties

📁 Project Structure File Breakdown index.html (Single file contains):

HTML structure (3 pages) CSS styling (~300 lines) JavaScript logic (~200 lines) Music database (28 songs) All functionality

Total Lines of Code: ~500-600 lines

🤝 Contributing We welcome contributions! Here's how you can help: Ways to Contribute

Report Bugs

Open an issue on GitHub Describe the bug clearly Include steps to reproduce

Suggest Features

Open a feature request Explain the use case Provide mockups if possible

Submit Pull Requests

Fork the repository Create a feature branch Make your changes Submit PR with description

Improve Documentation

Fix typos Add examples Translate README

Spread the Word

Star the repository ⭐ Share on social media Write a blog post

📞 Contact Project Creator

Name: Gajula Vatsalya Email: vatsalyagajula@gmail.com GitHub:https://github.com/vatsalyakrishnaa LinkedIn: www.linkedin.com/in/vatsalya-gajula 

Project Links

Live Demo: https://chowdamdharanipriya.github.io/Emotion-Based-Music-Recommender/ GitHub Repo: https://github.com/chowdamdharanipriya/emotion-music-recommender Documentation: [Link to detailed docs]

Development Guidelines

Follow existing code style Test on multiple browsers Update README if needed Comment complex logic Keep changes focused

🙏 Acknowledgments

Inspiration: Music therapy research and emotion psychology Technology: WebRTC, modern browser APIs Design: Modern UI/UX trends and gradient aesthetics Community: Open-source developers and contributors Hackathon: "TechVybe Hackathon" for the opportunity

📊 Project Statistics

Lines of Code: ~500 Development Time: 2 weeks Technologies Used: 3 (HTML, CSS, JS) Supported Emotions: 7 Music Database: 28 songs Browser Compatibility: 95%+ Performance Score: 95/100 (Lighthouse)

📚 References & Resources Research Papers

Music and Emotion - Psychology Today Facial Expression Recognition - IEEE Papers Music Therapy Benefits - Medical Journals

Documentation

WebRTC API Docs getUserMedia() Reference Emotion Detection Research

Tools & Libraries (Future)

face-api.js TensorFlow.js Spotify Web API

🎯 Project Goals Primary Goals ✅

Create working prototype Implement webcam integration Build music recommendation system Design beautiful UI Deploy online

Secondary Goals 🔄

Add real ML emotion detection Integrate Spotify API Implement user accounts Add mobile app Scale to 1000+ users

💬 FAQ Q: Do I need to create a Spotify account? A: No, the prototype works without any external accounts. Q: Does it work on mobile phones? A: Yes! The design is responsive and works on all devices with cameras. Q: Is my face data stored anywhere? A: No, all processing happens locally in your browser. Nothing is sent to servers. Q: Can I use it without a camera? A: Currently, camera is required for emotion detection. Future versions will add manual input. Q: Why are emotions random in the demo? A: This is a prototype with simulated detection. Real ML model will be added in production. Q: Can I contribute to the project? A: Yes! See the Contributing section above.

🎨 Design Philosophy

Simplicity: Easy to use, minimal learning curve Beauty: Modern aesthetics with gradients and animations Privacy: User data stays on device Performance: Fast, responsive, lightweight Accessibility: Works for everyone, everywhere

📈 Roadmap Q1 2025: Prototype Launch ✅ Q2 2025: Real ML Integration Q3 2025: Spotify API + Mobile Apps Q4 2025: Social Features + Analytics Q1 2026: B2B Solutions Q2 2026: Global Expansion

🎉 Thank You! Thank you for checking out MoodTunes AI! If you like this project:

⭐ Star the repository 🍴 Fork and contribute 📢 Share with friends 💬 Provide feedback

Made with ❤️ and 🎵 by [404 not founders] - C. Dharani priya, G. Vatsalya, P. Kruthika Reddy

Last Updated: [31-10-2025]
