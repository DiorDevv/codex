export default function ContactPage() {
  return (
    <div className="grid gap-8 md:grid-cols-[1.2fr_0.8fr]">
      <section className="card space-y-4">
        <h1 className="section-title">Contact</h1>
        <p className="text-sm text-white/70">
          Tell me about your project, timeline, and budget. I’ll reply within 24
          hours.
        </p>
        <form className="space-y-4">
          <input
            className="w-full rounded-xl border border-white/20 bg-transparent px-4 py-3 text-sm"
            placeholder="Your name"
          />
          <input
            className="w-full rounded-xl border border-white/20 bg-transparent px-4 py-3 text-sm"
            placeholder="Email"
            type="email"
          />
          <textarea
            className="w-full rounded-xl border border-white/20 bg-transparent px-4 py-3 text-sm"
            placeholder="Project details"
            rows={5}
          />
          <button className="rounded-full bg-white px-6 py-3 text-sm font-semibold text-black">
            Send message
          </button>
        </form>
      </section>
      <aside className="card space-y-4">
        <h2 className="section-title">Direct links</h2>
        <div className="space-y-2 text-sm text-white/70">
          <p>Telegram: @profolio</p>
          <p>Email: hello@profolio.dev</p>
          <p>LinkedIn: linkedin.com/in/profolio</p>
        </div>
      </aside>
    </div>
  );
}
