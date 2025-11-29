import { useEffect, useState } from "react";
import api from "../services/api";

export default function Experience() {
  const [exp, setExp] = useState([]);

  useEffect(() => {
    api.get("/experience/")
      .then(res => setExp(res.data))
      .catch(err => console.error(err));
  }, []);

  return (
    <div>
      <h1 className="text-3xl font-bold mb-6">Experience</h1>

      {exp.map((e) => (
        <div key={e.id} className="border p-4 rounded bg-white shadow mb-4">
          <h3 className="text-xl font-semibold">{e.role}</h3>
          <p>{e.company}</p>
          <p className="text-gray-600">{e.duration}</p>
        </div>
      ))}
    </div>
  );
}
