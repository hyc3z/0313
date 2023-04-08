class Point {
  final double x;
  final double y;
  static const String name = "Point";

  String toString() {
    return 'x:${x}, y:${y}';
  }

  Point(this.x, this.y) {}
}

void main() {
  List<int> list = [4, 5, 6];
  var halogens = {1, 2, 3, 1, for (var i in list) i};

  print([...halogens]);
  print(Point(list[0].toDouble(), list[1].toDouble()));
}
