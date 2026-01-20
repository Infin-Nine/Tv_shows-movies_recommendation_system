# # 🎬 Movie & TV Show Recommendation System

A **Content-Based Movie and TV Show Recommendation System** built using **Python, Machine Learning, and Streamlit**.  
The application recommends similar movies or TV shows based on user selection using **text similarity techniques**.

---

## ✨ Features

- 🎬 Movie Recommendations
- 📺 TV Show Recommendations
- Single unified Streamlit application
- Content-based filtering using similarity scores
- Movie & TV show posters fetched using **TMDB API**
- Clean and interactive UI


---
## ⚠️ TMDB API Access Notice (Important)

This project uses the **TMDB (The Movie Database) API** to fetch movie posters and additional movie details.

### ❗ Important Note for Users in India

Due to certain restrictions, **TMDB API access may be blocked in India**.  
As a result:

- Movie posters may not load
- The application may throw errors while fetching data from TMDB
- The app may not run as expected when poster fetching is enabled

<img width="700" height="591" alt="Screenshot 2026-01-19 154113" src="https://github.com/user-attachments/assets/1dd5b4ae-77ae-442b-9f12-a676a11851cc" />
<img width="700" height="591" alt="Screenshot 2026-01-19 154139" src="https://github.com/user-attachments/assets/0319ae43-3392-4762-88fb-fa8d3282645b" />

### ✅ Solution

To run the application **without errors** and to **successfully fetch movie posters**, please make sure to:

- Use a **VPN** while running the application
- Ensure the VPN allows access to TMDB services

Once the VPN is active, the application should work normally without any TMDB-related issues.

---

🔹 If you do not want to use a VPN, you can:
- Disable poster fetching logic in `app.py`, or
- Modify the app to run only with local data
