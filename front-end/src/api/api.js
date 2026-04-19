const API_URL = import.meta.env.VITE_API_BACKEND;

export const createPrediction = async (payload) => {
  const res = await fetch(`${API_URL}/api/predictions`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(payload),
  });

  const data = await res.json();

  if (!res.ok) {
    throw new Error(data?.detail || 'API error');
  }

  return data;
};

export async function explainPrediction(data) {
  const res = await fetch(`${API_URL}/api/predictions/chart`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
  });

  return res.json();
}
