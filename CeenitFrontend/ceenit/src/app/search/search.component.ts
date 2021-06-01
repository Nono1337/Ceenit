import { Component, OnInit } from '@angular/core';
import { HttpServiceService } from 'src/app/service/http-service.service';
import { ActivatedRoute } from '@angular/router';
import { MovieList } from '../Model/movie.model';
@Component({
  selector: 'app-search',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.css'],
})
export class SearchComponent implements OnInit {
  constructor(private httpServe: HttpServiceService, private route: ActivatedRoute) {}
  lstMovies: MovieList[];
  
  ngOnInit(): void {
    this.lstMovies = new Array<MovieList>();
    this.httpServe
      .getListMoviesByTitle(this.route.snapshot.paramMap.get('title'))
      .subscribe((resp) => {
        console.log(resp);
        if (resp != undefined) {
          // @ts-ignore: TS2339
          resp.forEach((movie) => {
            this.lstMovies.push(movie);
          });
        }
      });
  }
}
