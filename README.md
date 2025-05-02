# lstm-behavioral-clustering
A deep learning-based pipeline using LSTM autoencoders for behavioral clustering and performance analysis across dynamic environments and volatility levels.

This project leverages deep learning and clustering techniques to analyze human decision-making behavior in dynamic and uncertain environments. By training an LSTM autoencoder on participant trial data, we compress behavioral patterns into latent embeddings, which are then clustered and analyzed across different environmental conditions and volatility levels.

---

## 🚀 Project Goals

- 🔍 **Learn latent behavioral patterns** via LSTM autoencoders  
- 🧩 **Cluster participants** with similar decision-making strategies  
- 📊 **Visualize and analyze** group behavior over time  
- 🌍 **Compare performance** across different environments and volatility levels  
- 📈 **Run statistical tests** (ANOVA) for group differences  

---

## 📦 Dataset Overview

Each row in the dataset represents a trial for one participant in a multi-island choice task.

**Key Columns:**
- `Participant` – Unique participant ID  
- `Environment_Type` – {High-Fast, High-Slow, Low-Fast, Low-Slow}  
- `Chosen_Island`, `Reward`, `Score`, `Response_Time`  
- `Win-Stay`, `Lose-Shift`, `Exploration`, `Exploitation`  

📁 Place the CSV file at:
data/Complete game data csv(modified envo)38participents.csv

---

## 🧠 Methodology Overview

### 🔧 1. Preprocessing
- Normalize numeric features
- Encode categorical variables
- Convert trials into fixed-length sequences per participant

### 🔄 2. LSTM Autoencoder
- Compress participant behavior into dense latent vectors
- Minimize reconstruction loss (MSE)

### 📉 3. Dimensionality Reduction
- Use **t-SNE** and **UMAP** for 2D projection of embeddings

### 🧩 4. Clustering
- Apply **K-Means** to group participants (3 clusters)
- Visualize with labels and participant IDs

### 📈 5. Cluster Behavior Analysis
- Track behavior over time across clusters
- Label groups (e.g., Explorers, Exploiters, Balanced)

### 🌍 6. Environment & Volatility Effects
- Compare group performance across:
  - 4 environment types
  - 2 volatility levels (High/Low)
- Use **ANOVA** to detect statistical differences

---

## 📊 Example Outputs

- ✅ Clustered participant visualizations (t-SNE, UMAP)
- 📈 Feature trends over time by group
- 📊 Bar and box plots by environment type
- 🧪 ANOVA tables for group comparisons

---

## ⚙️ Installation & Usage

### 🔁 Step 1: Clone this repo

```bash
git clone https://github.com/yourusername/lstm-behavioral-clustering.git
cd lstm-behavioral-clustering


📂 Repository Structure
bash
Copy
Edit
.
├── final_one_lstm.py                 # Full pipeline script
├── Final_one_lstm.ipynb             # Colab notebook version
├── README.md                        # Project documentation
├── requirements.txt                 # Dependencies
├── .gitignore                       # Ignore unnecessary files
└── data/
    └── Complete game data csv(...)  # Input dataset (add manually)
