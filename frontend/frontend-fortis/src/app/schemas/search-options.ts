export class SearchOptions {
  text: string;
  tags: string[];

  constructor(text: string, tags: string[]) {
    this.text = text
    this.tags = tags;
  }
}
