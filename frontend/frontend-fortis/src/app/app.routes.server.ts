import { RenderMode, ServerRoute } from '@angular/ssr';

export const serverRoutes: ServerRoute[] = [
  {
    path: '**',
    renderMode: RenderMode.Prerender
  },
  {
    path: 'review/:id',
    renderMode: RenderMode.Server
  },
  {
    path: 'edit-request/:id',
    renderMode: RenderMode.Server
  }
];
