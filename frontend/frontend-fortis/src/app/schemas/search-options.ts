export class SearchOptions {
  text: string;
  tags: string[];
  category: string | null;
  order: string | null;

  constructor(text: string, tags: string[], category: string | null = null, order: string | null) {
    this.text = text
    this.tags = tags;
    this.category = category;
    this.order = order;
  }
}
