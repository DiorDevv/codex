const posts = [
  {
    title: "Designing for conversions",
    date: "Feb 14, 2024",
    readTime: "6 min",
    tag: "UX",
  },
  {
    title: "Scaling FastAPI services",
    date: "Jan 28, 2024",
    readTime: "8 min",
    tag: "Backend",
  },
];

export default function BlogPage() {
  return (
    <div className="space-y-10">
      <div>
        <h1 className="section-title">Blog</h1>
        <p className="text-sm text-white/70">
          Thoughts on design systems, product strategy, and engineering.
        </p>
      </div>

      <div className="grid gap-6 md:grid-cols-2">
        {posts.map((post) => (
          <article key={post.title} className="card space-y-3">
            <p className="text-xs uppercase tracking-[0.2em] text-white/50">
              {post.tag}
            </p>
            <h2 className="text-lg font-semibold">{post.title}</h2>
            <p className="text-xs text-white/60">
              {post.date} · {post.readTime}
            </p>
            <button className="text-sm font-semibold text-white/80">
              Read story →
            </button>
          </article>
        ))}
      </div>
    </div>
  );
}
