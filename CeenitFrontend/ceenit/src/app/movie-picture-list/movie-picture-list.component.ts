import { Component, OnInit } from '@angular/core';
import { HttpServiceService } from 'src/app/service/http-service.service';
import { ActivatedRoute } from '@angular/router';
import { HottestMovie } from '../Model/HottestMovie.model';
import { asLiteral } from '@angular/compiler/src/render3/view/util';

@Component({
  selector: 'app-movie-picture-list',
  templateUrl: './movie-picture-list.component.html',
  styleUrls: ['./movie-picture-list.component.css']
})

export class MoviePictureListComponent implements OnInit {

  constructor(private httpServe: HttpServiceService, private route: ActivatedRoute) {}
  hotMovies: HottestMovie[];

  ngOnInit(): void {
    this.hotMovies = new Array<HottestMovie>();
    this.httpServe
      .getFiveHottestMovies()
      .subscribe((resp) => {
        console.log(resp);
        if (resp != undefined) {
          // @ts-ignore: TS2339
          resp.forEach((movie) => {
            this.hotMovies.push(movie);
          });
        }
      });
  }

  show(): void {
    alert('Info')
  }

  toggle(event) {
    console.log(event.target); 
 }
}

export interface Tile {
  title: string;
  picture: string;
}
