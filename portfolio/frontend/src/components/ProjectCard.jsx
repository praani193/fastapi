export default function ProjectCard({ title, description }) {
return (
<div className="bg-white shadow p-5 rounded-lg border">
<h3 className="text-xl font-semibold mb-2">{title}</h3>
<p>{description}</p>
</div>
)
}