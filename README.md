# 🎬 TMDB Movie Recommender System

Welcome to the **TMDB Movie Recommender System**! This project is designed to provide personalized movie recommendations based on a user's selected movie. Using data from **TMDB (The Movie Database)**, it suggests similar movies and displays their posters. 🚀

## 📋 Project Overview

This recommender system leverages **cosine similarity** to find movies similar to the one selected by the user. It uses the movie dataset from TMDB and the movie poster images are fetched via the TMDB API. The user interface is built using **Streamlit**.

## 🔧 Features

- **Select a movie**: Pick a movie from the dropdown list.
- **Get recommendations**: The system will show you 5 movies similar to your selected movie, with their posters displayed.
- **Simple & User-friendly**: Easy-to-use interface powered by Streamlit.

## 📦 How It Works

1. **Dataset**: A preprocessed dataset (`movie_dict.pkl`) containing movie information (titles, movie IDs) is loaded.
2. **Similarity Matrix**: The similarity matrix (`similarity.pkl`) computes the cosine similarity between movies.
3. **API Integration**: The system fetches movie posters using the TMDB API.
4. **Recommendation**: Based on your selected movie, the system suggests 5 similar movies and displays their posters.

## 🛠️ Tech Stack

- **Python** 🐍
- **Pandas** for data handling
- **Pickle** for loading preprocessed data
- **Streamlit** for the web app interface
- **TMDB API** for fetching movie posters

## ⚙️ How to Run the Project

1. **Clone the repository**:
   ```bash
   git clone <repository_url>
   ```
   
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app**:
   ```bash
   streamlit run app.py
   ```

4. **Enjoy the movie recommendations!** 🍿

## 🌐 API Configuration

The movie posters are fetched using the TMDB API. You need an **API key** from TMDB. Replace the API key in the code with your own to fetch posters:

```python
Authorization: "Bearer YOUR_TMDB_API_KEY"
```

## 📂 Project Structure

- `app.py`: Contains the main application logic using Streamlit.
- `movie_dict.pkl`: Preprocessed movie data.
- `similarity.pkl`: Precomputed similarity matrix for recommending movies.
- `requirements.txt`: Dependencies required to run the project.

## 🖼️ Example

1. **Select a movie** from the dropdown:
   ![Movie Selection](screenshot_1.png)

2. **Get Recommendations** with posters:
   ![Recommendations](screenshot_2.png)

## 💡 Future Improvements

- Add more features like genre filtering or search functionality.
- Include ratings or reviews in recommendations.
- Improve the model with more advanced machine learning techniques.

## 📬 Contact

If you have any questions or suggestions, feel free to reach out!
