export default function ProjectDetailPage() {
  return (
    <div className="space-y-10">
      <div className="card space-y-4">
        <p className="text-xs uppercase tracking-[0.2em] text-white/50">
          Case study
        </p>
        <h1 className="section-title">SaaS Dashboard</h1>
        <p className="text-sm text-white/70">
          A complete product analytics dashboard with subscription management,
          customer insights, and automated reports.
        </p>
        <div className="flex flex-wrap gap-3 text-xs text-white/60">
          <span className="rounded-full border border-white/20 px-3 py-1">
            Next.js
          </span>
          <span className="rounded-full border border-white/20 px-3 py-1">
            FastAPI
          </span>
          <span className="rounded-full border border-white/20 px-3 py-1">
            PostgreSQL
          </span>
        </div>
      </div>

      <section className="grid gap-6 md:grid-cols-2">
        <div className="card space-y-4">
          <h2 className="section-title">Highlights</h2>
          <ul className="list-disc space-y-2 pl-5 text-sm text-white/70">
            <li>Dynamic charting with live metrics.</li>
            <li>Role-based access with JWT authentication.</li>
            <li>Automated PDF exports for executives.</li>
          </ul>
        </div>
        <div className="card space-y-4">
          <h2 className="section-title">Links</h2>
          <div className="flex flex-col gap-3 text-sm text-white/70">
            <a className="underline" href="#">
              GitHub repository
            </a>
            <a className="underline" href="#">
              Live demo
            </a>
          </div>
        </div>
      </section>
    </div>
  );
}
