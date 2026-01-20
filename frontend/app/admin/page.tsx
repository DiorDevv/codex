export default function AdminPage() {
  return (
    <div className="space-y-6">
      <div className="card space-y-3">
        <h1 className="section-title">Admin Console</h1>
        <p className="text-sm text-white/70">
          Log in with JWT to manage projects, blog posts, skills, and site
          settings.
        </p>
      </div>
      <div className="grid gap-6 md:grid-cols-2">
        <div className="card space-y-3">
          <h2 className="text-lg font-semibold">Content</h2>
          <ul className="text-sm text-white/70">
            <li>Projects CRUD</li>
            <li>Blog posts CRUD</li>
            <li>Tags and testimonials</li>
          </ul>
        </div>
        <div className="card space-y-3">
          <h2 className="text-lg font-semibold">Settings</h2>
          <ul className="text-sm text-white/70">
            <li>Site profile</li>
            <li>Social links</li>
            <li>Media uploads</li>
          </ul>
        </div>
      </div>
    </div>
  );
}
