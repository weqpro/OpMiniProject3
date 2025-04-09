export class AidRequest{
  id: number;
  name: string;
  description: string;
  image: string;
  endDate: Date;
  location: string;
  tags: string[];
  status: string;
  soldierId: number;
  categoryId: number;

  constructor(
    id: number,
    name: string,
    description: string,
    image: string,
    endDate: Date,
    location: string,
    tags: string[],
    status: string,
    soldierId: number,
    categoryId: number
  ) {
    this.id = id;
    this.name = name;
    this.description = description;
    this.image = image;
    this.endDate = endDate;
    this.location = location;
    this.tags = tags;
    this.status = status;
    this.soldierId = soldierId;
    this.categoryId = categoryId;
  }
}
