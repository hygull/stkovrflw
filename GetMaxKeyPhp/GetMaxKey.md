**@Niki**, above answers are appreciable. Here I've tried to present you in my way. May be, it can be similar to other answers. I will try to find other ways to do the same and update the answer.

> Try it online at http://rextester.com/MDGZ18118.

### PHP code &raquo;

    <?php //php 7.0.8

        $arr1 = Array
        (
            "anger" => 0,
            "disgust" => 20,
            "fear" => 0,
            "joy" => 22.853,
            "sadness" => 0,
            "surprise" => 0,
        );

        $arr2 = Array
        (
            "anger" => 0,
            "disgust" => 20,
            "fear" => 0,
            "joy" => 22.853,
            "sadness" => 0,
            "surprise" => 0,
        );
          
        $ret = print_r($arr1); // print_r() returns 1, if we will not store it in any variable then it will be printed on screen.
        echo "\n"; // echo "<br>"; for browser
        $ret = print_r($arr2);

        // Finding key of max element
        echo array_search(max($arr1), $arr1);
        echo("\n"); // echo "<br>"; for browser
        echo array_search(max($arr2), $arr2);
    ?>

### Output &rquo; 

    Array
    (
        [anger] => 0
        [disgust] => 20
        [fear] => 0
        [joy] => 22.853
        [sadness] => 0
        [surprise] => 0
    )

    Array
    (
        [anger] => 0
        [disgust] => 20
        [fear] => 0
        [joy] => 22.853
        [sadness] => 0
        [surprise] => 0
    )
    joy
    joy