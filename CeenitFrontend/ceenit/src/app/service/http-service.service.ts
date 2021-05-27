import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root',
})
export class HttpServiceService {
  constructor(private http: HttpClient) {}

  public getListMoviesByTitle(searchTitle: string) {
    return this.http.get('/movie-backend/movie/search/' + searchTitle);
  }

  public getFiveHottestMovies() {
    return this.http.get('/movie-backend/movie/getFiveHottest');
  
  }
  
  public getMovieDetailsById(movieId) {
    return this.http.get('/movie-backend/movie/detail/'+ movieId)
  }

  /**
   * getWatchlistByUserID
   */
  public getWatchlistByUserID() {
    
  }

  public getMovieLists(){
    return this.http.get('/movie-backend/movie/getMovieLists');
  }
}
