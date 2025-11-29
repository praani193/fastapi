export default function ExperienceCard({ title, company, duration }) {
return (
<div className="bg-white border p-4 rounded shadow">
<h3 className="text-xl font-semibold">{title}</h3>
<p>{company}</p>
<p className="text-sm text-gray-600">{duration}</p>
</div>
)
}