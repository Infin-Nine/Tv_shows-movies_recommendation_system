# movie_recommendation_system

A **Content-Based Movie Recommendation System** built using **Python, Machine Learning, and Streamlit**.  
This app recommends movies similar to the one selected by the user based on **text similarity**.

---

## 📌 What does this project do?

- Takes a movie name as input
- Finds movies **similar in content**
- Recommends **top 5 similar movies**
- Runs as a **web application using Streamlit**

---
## ⚠️ TMDB API Access Notice (Important)

This project uses the **TMDB (The Movie Database) API** to fetch movie posters and additional movie details.

### ❗ Important Note for Users in India

Due to certain restrictions, **TMDB API access may be blocked in India**.  
As a result:

- Movie posters may not load
- The application may throw errors while fetching data from TMDB
- The app may not run as expected when poster fetching is enabled

### ✅ Solution

To run the application **without errors** and to **successfully fetch movie posters**, please make sure to:

- Use a **VPN** while running the application
- Ensure the VPN allows access to TMDB services

Once the VPN is active, the application should work normally without any TMDB-related issues.

---

🔹 If you do not want to use a VPN, you can:
- Disable poster fetching logic in `app.py`, or
- Modify the app to run only with local data
