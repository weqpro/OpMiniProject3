export class SearchOptions {
  text: string;
  tags: string[];
  category: string | null;

  constructor(text: string, tags: string[], category: string | null = null) {
    this.text = text
    this.tags = tags;
    this.category = category;
  }
}
