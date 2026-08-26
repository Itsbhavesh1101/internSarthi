/**
 * Centralized API Configuration for internSarthi
 * Dynamically switches between local backend (http://127.0.0.1:8001) and production (Render).
 */
const getApiBaseUrl = () => {
  if (window.INTERNSARTHI_API_URL) {
    return window.INTERNSARTHI_API_URL;
  }
  const hostname = window.location.hostname;
  if (hostname === "localhost" || hostname === "127.0.0.1" || hostname === "") {
    return "http://127.0.0.1:8001";
  }
  return "https://internsarthi-hhn7.onrender.com";
};

const API_BASE_URL = getApiBaseUrl();
