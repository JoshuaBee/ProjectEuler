const version = "1.09";
const cacheName = "jb-${version}";

self.addEventListener("install", e => {
	console.log('Service worker installing...');
	e.waitUntil(
		caches.open(cacheName).then(cache => {
			return cache.addAll([
				"/",
				"/index.html",
				"/manifest.webmanifest",
				"/sitemap.xml",
				"/1/index.html",
				"/2/index.html",
				"/3/index.html",
				"/4/index.html",
				"/5/index.html",
				"/6/index.html",
				"/7/index.html",
				"/8/index.html",
				"/9/index.html",
				"/10/index.html",
				"/11/index.html",
				"/12/index.html",
				"/13/index.html",
				"/14/index.html",
				"/15/index.html",
				"/16/index.html",
				"/images/icons/arrow-back-24.svg",
				"/images/logos/company-logo-192.png",
				"/images/logos/company-logo-192.svg",
				"/images/logos/company-logo-512.png",
				"/images/logos/company-logo-512.svg",
				"/images/logos/logo-192.png",
				"/images/logos/logo-192.svg",
				"/images/logos/logo-512.png",
				"/images/logos/logo-512.svg",
				"/images/screenshots/screenshot1.webp",
				"/scripts/main.js",
				"/styles/1-settings/color.css",
				"/styles/3-generic/reset.css",
				"/styles/4-elements/body.css",
				"/styles/4-elements/iframe.css",
				"/styles/4-elements/section.css",
				"/styles/6-components/button.css",
				"/styles/6-components/content.css",
				"/styles/6-components/footer.css",
				"/styles/6-components/grid.css",
				"/styles/6-components/header.css",
				"/styles/7-utilities/color.css",
				"/styles/7-utilities/text-alignment.css"
			])
			.then(() => self.skipWaiting());
		})
	);
});

self.addEventListener("activate", event => {
	console.log('Service worker activating...');
	event.waitUntil(self.clients.claim());
});

self.addEventListener("fetch", event => {
	console.log('Service worker fetching:', event.request.url);
	event.respondWith(
		caches.open(cacheName)
		.then(cache => cache.match(event.request, {ignoreSearch: true}))
		.then(response => {
			return response || fetch(event.request);
		})
	);
});
