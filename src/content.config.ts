import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const blog = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/blog' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    pubDate: z.coerce.date(),
    category: z.string(),
    tags: z.array(z.string()).optional(),
    image: z.string().optional(),
    author: z.string().default('三狮生物分子诊断技术团队'),
    jsonLd: z.any().optional(),
  }),
});

const blogEn = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/blog-en' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    pubDate: z.coerce.date(),
    category: z.string(),
    tags: z.array(z.string()).optional(),
    image: z.string().optional(),
    author: z.string().default('Sanshi Bio Molecular Diagnostics Team'),
    jsonLd: z.any().optional(),
  }),
});

export const collections = { blog, blogEn };
