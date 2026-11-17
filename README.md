# 🪺 WebNest

**WebNest** is a lightweight Python library designed for Data Scientists and Jupyter Notebook users. It eliminates context switching by allowing you to seamlessly render live HTTPS websites, external documentation, and YouTube tutorials directly inside your `.ipynb` output cells.

Compatible with **Jupyter Notebook**, **JupyterLab**, and **Google Colab**.

---

## ✨ Features

* **Zero Context Switching:** Read documentation, API references, and articles right next to your code.
* **YouTube Video Embedding:** Watch tutorials and lectures directly within your notebook cells with clean, responsive framing.
* **Lightweight & Fast:** Minimal dependencies so your environment stays clean and fast.
* **Cross-Platform Notebook Support:** Works out-of-the-box in Jupyter Notebook, JupyterLab, and Google Colab.
* **Customizable Dimensions:** Easily adjust the width and height of your embedded frames to fit your screen layout.

---

## 📦 Installation

Install WebNest directly from PyPI using `pip`:

```bash
pip install webnest
```

---

## 🚀 Quick Start

Import `webnest` into your notebook and start embedding web pages or videos with a single line of code.

### 1. Embed a Website or Documentation

Render any HTTPS-enabled website (such as Pandas, Scikit-Learn, or PyTorch docs) directly in your cell output:

```python
import webnest

# Render official documentation inside the notebook
webnest.open("https://pandas.pydata.org/docs/")
```

### 2. Customizing Frame Dimensions

Adjust the `width` and `height` parameters (in pixels or percentages) to suit your workspace:

```python
import webnest

webnest.open(
    url="https://scikit-learn.org/stable/",
    width="100%",
    height=600
)
```

### 3. Embed a YouTube Video

Pass a standard YouTube URL to embed a playable video tutorial directly below your code:

```python
import webnest

# Embed a tutorial video
webnest.youtube("https://www.youtube.com/watch?v=dQw4w9WgXcQ", width=800, height=450)
```

---

## 🛠️ API Reference

### `webnest.open(url, width="100%", height=500)`
Renders an external HTTPS webpage inside an `IFrame`.

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `url` | `str` | *Required* | The HTTPS URL of the webpage you want to display. |
| `width` | `str` or `int` | `"100%"` | Width of the embedded frame (e.g., `"100%"` or `800`). |
| `height` | `str` or `int` | `500` | Height of the embedded frame in pixels. |

### `webnest.youtube(url, width=720, height=405)`
Automatically parses a YouTube link and embeds a clean, playable video frame.

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `url` | `str` | *Required* | Standard YouTube watch URL or short `youtu.be` link. |
| `width` | `int` | `720` | Width of the video player in pixels. |
| `height` | `int` | `405` | Height of the video player in pixels. |

---

## ⚠️ Limitations & Notes

* **HTTPS Requirement:** Modern browsers block mixed content. Target URLs must use `https://`.
* **X-Frame-Options:** Some websites (e.g., GitHub, Google Search, StackOverflow) explicitly block embedding via `X-Frame-Options` or `Content-Security-Policy` headers. If a site refuses to connect, it is due to the host server's security policy.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! 

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.