import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-movie-picture-list',
  templateUrl: './movie-picture-list.component.html',
  styleUrls: ['./movie-picture-list.component.css']
})
export class MoviePictureListComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
  }

  tiles: Tile[] = [
    {title: 'Movie Title', picture: 'https://i.pinimg.com/originals/6c/0f/d1/6c0fd186a12815a51ce2e3298f6ab9cd.jpg'},
    {title: 'Among Us', picture: 'https://i.redd.it/3trl9ojxiop51.png'},
    {title: 'Godzilla', picture: 'https://cdn20.pamono.com/p/z/7/2/728702_agebtldars/vintage-french-godzilla-film-movie-poster-by-a-poucel-1954-1.jpg'},
    {title: 'Hacker', picture: 'https://www.arthipo.com/image/cache/catalog/poster/movie/759-1554/pfilm1491-hacker_7cf19a97-poster-movie-film-1000x1000.jpg'},
    {title: 'Shrek3', picture: 'https://i.pinimg.com/originals/24/ea/a8/24eaa8b4e85cc578238ed903bf2494d6.jpg'},
  ];
}

export interface Tile {
  title: string;
  picture: string;
}
