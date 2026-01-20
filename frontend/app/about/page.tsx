const timeline = [
  {
    year: "2020",
    title: "Started freelancing",
    description: "Delivered MVPs for startups in health and fintech.",
  },
  {
    year: "2022",
    title: "Lead developer",
    description: "Scaled a multi-tenant SaaS to 20k+ users.",
  },
  {
    year: "2024",
    title: "ProFolio launch",
    description: "Curated a full-stack portfolio for global clients.",
  },
];

const stack = ["FastAPI", "Next.js", "PostgreSQL", "Tailwind", "Docker", "AWS"];

export default function AboutPage() {
  return (
    <div className="space-y-12">
      <section className="card space-y-4">
        <h1 className="section-title">About me</h1>
        <p className="text-sm text-white/70">
          I’m a full-stack developer focused on crafting premium digital
          experiences. I blend backend performance with frontend polish to build
          products that feel effortless.
        </p>
        <button className="rounded-full border border-white/30 px-6 py-3 text-sm font-semibold">
          Download CV
        </button>
      </section>

      <section className="grid gap-6 md:grid-cols-2">
        <div className="card space-y-4">
          <h2 className="section-title">Timeline</h2>
          <div className="space-y-4">
            {timeline.map((item) => (
              <div key={item.year} className="border-b border-white/10 pb-4">
                <p className="text-xs uppercase tracking-[0.2em] text-white/50">
                  {item.year}
                </p>
                <h3 className="text-lg font-semibold">{item.title}</h3>
                <p className="text-sm text-white/70">{item.description}</p>
              </div>
            ))}
          </div>
        </div>
        <div className="card space-y-4">
          <h2 className="section-title">Tech stack</h2>
          <div className="flex flex-wrap gap-3">
            {stack.map((item) => (
              <span
                key={item}
                className="rounded-full border border-white/20 px-4 py-2 text-xs uppercase tracking-[0.2em] text-white/70"
              >
                {item}
              </span>
            ))}
          </div>
        </div>
      </section>
    </div>
  );
}
