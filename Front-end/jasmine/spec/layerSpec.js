/**
 * Created by yigoss on 10/8/14.
 */
describe("Test one function in layer.js in shouchela.com", function() {
//    beforeEach(function() {
//      player.play(song);
//      player.pause();
//    });

    SetParamter = new SetGetParameter();

    it("First Case", function() {

      currentUrl = "www.souchela.com#?para1=12"
      expect(SetParamter.setUrl(currentUrl,1,2)).toEqual("www.souchela.com?1=2&para1=12");

      // demonstrates use of 'not' with a custom matcher
    });

//    it("should be possible to resume", function() {
//      player.resume();
//      expect(player.isPlaying).toBeTruthy();
//      expect(player.currentlyPlayingSong).toEqual(song);
//    });
  });