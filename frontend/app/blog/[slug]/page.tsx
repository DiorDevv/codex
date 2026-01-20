export default function BlogDetailPage() {
  return (
    <article className="space-y-8">
      <header className="card space-y-3">
        <p className="text-xs uppercase tracking-[0.2em] text-white/50">
          Backend
        </p>
        <h1 className="section-title">Scaling FastAPI services</h1>
        <p className="text-sm text-white/70">
          Practical steps to keep FastAPI services fast, resilient, and
          observable.
        </p>
        <p className="text-xs text-white/60">Jan 28, 2024 · 8 min read</p>
      </header>
      <section className="card space-y-4 text-sm text-white/70">
        <p>
          Focus on async boundaries, connection pooling, and caching strategies.
          Treat every endpoint like a product surface.
        </p>
        <p>
          Add structured logging, protect critical endpoints with rate limits,
          and ship dashboards that visualize p95 latency.
        </p>
      </section>
    </article>
  );
}
