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
