# 1) build stage
FROM node:18-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build -- --configuration production

# 2) serve stage
FROM nginx:stable-alpine
COPY --from=builder /app/dist/frontend-fortis/browser /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf
