import { useState, useEffect } from "react";
const API_BASE_URL = import.meta.env.VITE_API_URL;
import axios from 'axios';
import Cookies from 'js-cookie';

export const getCookie = (name) => {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(";").shift();
  return "";
};

// ✅ Function to Refresh CSRF Token

// Original
export const refreshCsrfToken = async () => {
  try {
    const response = await fetch(`${API_BASE_URL}/get_csrf_token/`, {
      method: "GET",
      credentials: "include",
    });

    // Extract token from cookie instead of headers
    const token = getCookie("csrftoken");
    console.log("token", token);
    if (token) {
      localStorage.setItem("csrftoken", token);
      return token;
    }
  } catch (error) {
    console.error("Failed to refresh CSRF token:", error);
  }
  return null;
};

// ✅ Custom Hook to Use CSRF Token

// Original
export const useCsrfToken = () => {
  const [csrfToken, setCsrfToken] = useState(localStorage.getItem("csrftoken") || "");

  useEffect(() => {
    if (!csrfToken) {
      refreshCsrfToken().then(setCsrfToken);
    }
  }, [csrfToken]);

  return csrfToken;
};

// ✅ CSRF Token Component for Forms
const CSRFTOKEN = () => {
  const csrfToken = useCsrfToken();
  return <input name="csrfmiddlewaretoken" value={csrfToken || ""} type="hidden" />;
};

export default CSRFTOKEN;

