const projects = [
  {
    title: "Fintech Landing",
    category: "Frontend",
    stack: "Next.js, Tailwind",
    description: "Conversion-focused marketing site with animations.",
  },
  {
    title: "CRM Platform",
    category: "Backend",
    stack: "FastAPI, PostgreSQL",
    description: "Role-based CRM with analytics and exports.",
  },
  {
    title: "Logistics Dashboard",
    category: "Full-stack",
    stack: "React, FastAPI",
    description: "Real-time tracking and fleet insights.",
  },
];

export default function ProjectsPage() {
  return (
    <div className="space-y-10">
      <div className="flex flex-wrap items-center justify-between gap-4">
        <div>
          <h1 className="section-title">Projects</h1>
          <p className="text-sm text-white/70">
            Filter by stack, browse, and deep dive into case studies.
          </p>
        </div>
        <div className="flex gap-3">
          <input
            className="rounded-full border border-white/20 bg-transparent px-4 py-2 text-sm"
            placeholder="Search project"
          />
          <select className="rounded-full border border-white/20 bg-transparent px-4 py-2 text-sm">
            <option>All categories</option>
            <option>Frontend</option>
            <option>Backend</option>
            <option>Full-stack</option>
          </select>
        </div>
      </div>

      <div className="grid gap-6 md:grid-cols-3">
        {projects.map((project) => (
          <article key={project.title} className="card space-y-3">
            <p className="text-xs uppercase tracking-[0.2em] text-white/50">
              {project.category}
            </p>
            <h2 className="text-lg font-semibold">{project.title}</h2>
            <p className="text-xs text-white/60">{project.stack}</p>
            <p className="text-sm text-white/70">{project.description}</p>
            <button className="text-sm font-semibold text-white/80">
              View details →
            </button>
          </article>
        ))}
      </div>
    </div>
  );
}
