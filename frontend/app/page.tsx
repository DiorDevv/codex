const featuredProjects = [
  {
    title: "SaaS Dashboard",
    stack: "Next.js · Tailwind",
    description: "Analytics dashboard with real-time charts and billing.",
  },
  {
    title: "E-commerce API",
    stack: "FastAPI · PostgreSQL",
    description: "Scalable backend with payment integration.",
  },
  {
    title: "Design System",
    stack: "React · Storybook",
    description: "Reusable UI kit with accessibility baked in.",
  },
];

const testimonials = [
  {
    name: "Madina S.",
    role: "Product Lead",
    text: "Clean design, fast delivery, and perfect communication.",
  },
  {
    name: "Aziz R.",
    role: "Founder",
    text: "Our portfolio conversion doubled after launch.",
  },
];

export default function HomePage() {
  return (
    <div className="space-y-16">
      <section className="grid gap-10 lg:grid-cols-[1.2fr_0.8fr]">
        <div className="space-y-6">
          <p className="text-sm uppercase tracking-[0.2em] text-white/60">
            Full-stack developer
          </p>
          <h1 className="text-4xl font-semibold md:text-6xl">
            Build premium products with a personal touch.
          </h1>
          <p className="text-lg text-white/70">
            ProFolio is a modern portfolio experience showcasing projects, blog
            stories, and an admin hub to manage your brand.
          </p>
          <div className="flex flex-wrap gap-4">
            <button className="rounded-full bg-white px-6 py-3 text-sm font-semibold text-black">
              Hire me
            </button>
            <button className="rounded-full border border-white/30 px-6 py-3 text-sm font-semibold">
              See projects
            </button>
          </div>
        </div>
        <div className="card space-y-6">
          <div>
            <p className="text-sm text-white/60">Quick stats</p>
            <div className="mt-4 grid gap-4 sm:grid-cols-3">
              <div>
                <p className="text-2xl font-semibold">5+</p>
                <p className="text-xs text-white/60">Years experience</p>
              </div>
              <div>
                <p className="text-2xl font-semibold">40+</p>
                <p className="text-xs text-white/60">Projects shipped</p>
              </div>
              <div>
                <p className="text-2xl font-semibold">12</p>
                <p className="text-xs text-white/60">Happy clients</p>
              </div>
            </div>
          </div>
          <div className="rounded-2xl bg-white/10 p-4">
            <p className="text-sm text-white/70">
              Available for freelance & full-time roles. Let’s build something
              unforgettable.
            </p>
          </div>
        </div>
      </section>

      <section className="space-y-6">
        <h2 className="section-title">Featured projects</h2>
        <div className="grid gap-6 md:grid-cols-3">
          {featuredProjects.map((project) => (
            <article key={project.title} className="card space-y-3">
              <h3 className="text-lg font-semibold">{project.title}</h3>
              <p className="text-xs uppercase tracking-[0.2em] text-white/60">
                {project.stack}
              </p>
              <p className="text-sm text-white/70">{project.description}</p>
              <button className="text-sm font-semibold text-white/80">
                View case study →
              </button>
            </article>
          ))}
        </div>
      </section>

      <section className="grid gap-6 md:grid-cols-2">
        <div className="card space-y-4">
          <h2 className="section-title">Testimonials</h2>
          <div className="space-y-4">
            {testimonials.map((testimonial) => (
              <div key={testimonial.name}>
                <p className="text-sm text-white/70">“{testimonial.text}”</p>
                <p className="mt-2 text-xs uppercase tracking-[0.2em] text-white/50">
                  {testimonial.name} · {testimonial.role}
                </p>
              </div>
            ))}
          </div>
        </div>
        <div className="card space-y-4">
          <h2 className="section-title">Let’s collaborate</h2>
          <p className="text-sm text-white/70">
            Share your idea and I’ll reply with a proposal, timeline, and launch
            plan.
          </p>
          <button className="rounded-full bg-white px-6 py-3 text-sm font-semibold text-black">
            Contact me
          </button>
        </div>
      </section>
    </div>
  );
}
