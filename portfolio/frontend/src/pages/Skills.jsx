import { useEffect, useState } from "react";
import api from "../services/api";

export default function Skills() {
  const [skills, setSkills] = useState([]);

  useEffect(() => {
    api.get("/skills/")
      .then(res => setSkills(res.data))
      .catch(err => console.error(err));
  }, []);

  return (
    <div>
      <h1 className="text-3xl font-bold mb-6">Skills</h1>

      <ul className="list-disc ml-6 text-lg">
        {skills.map((s) => (
          <li key={s.id}>{s.name}</li>
        ))}
      </ul>
    </div>
  );
}
