import { useState } from "react";
import api from "../services/api";

export default function Contact() {
  const [msg, setMsg] = useState("");

  const submitForm = () => {
    api.post("/contact/", { message: msg })
      .then(() => alert("Message sent!"))
      .catch(() => alert("Error"));
  };

  return (
    <div>
      <h1 className="text-3xl font-bold mb-6">Contact</h1>

      <textarea
        className="border p-3 w-full rounded"
        rows="5"
        placeholder="Write your message..."
        value={msg}
        onChange={(e) => setMsg(e.target.value)}
      />

      <button
        onClick={submitForm}
        className="bg-black text-white px-6 py-2 rounded mt-4"
      >
        Send
      </button>
    </div>
  );
}
