# Front-end

Vite + React UI for the Fashion Category Prediction app.

## Project Structure

```
front-end/
├── .env
├── index.html
├── src/
│   ├── api/
│   │   └── api.js
│   ├── assets/
│   │   └── avatar.jpg
│   ├── components/
│   │   ├── Chart.jsx
│   │   ├── Home.jsx
│   │   ├── ProductItem.jsx
│   │   └── TwoChartsSkeleton.jsx
│   ├── App.css
│   ├── App.jsx
│   └── main.jsx
├── package.json
└── vite.config.js
```

---

## Setup

### 1. Install dependencies

```bash
npm install
```

### 2. Configure environment

Create or update `.env` as needed (see the project root for required variables).

Example `.env`:

```bash
VITE_API_BACKEND=http://127.0.0.1:8001
```

### 3. Start the dev server

```bash
npm run dev
```

---

## Build and Preview

```bash
npm run build
npm run preview
```

---

## Deployment Notes

- Ensure the API base URL in `.env` points to the correct backend host.
- If you use a reverse proxy, update the backend URL accordingly.
