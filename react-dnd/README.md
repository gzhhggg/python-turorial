## React DnDの調査

### メンテナンスの観点

最終Commitが1年前になっているため、メンテナンスはされてそう
最終コミット日は2023年1月20日
※ もうこの時点でなしかも。。

###　パッケージインストール

```
npx create-react-app react-dnd --template typescript
cd react-dnd
npm install react-dnd react-dnd-html5-backend
```

### 手順

親コンポーネントでドラッグ＆ドロップを使いたい範囲をDndProviderでラップする
```
import React from "react";
import { DndProvider } from "react-dnd";
import { HTML5Backend } from "react-dnd-html5-backend";
import { Example } from "./Example";

export default function App() {
  return (
    <div className="App">
      <DndProvider backend={HTML5Backend}>
        <Example />
      </DndProvider>
    </div>
  );
}
```

ドラッグ制御の実装
ドラッグするコンポーネントに対して、useDragというhooksを使う

引数でtopとleftの座標を渡す
```
  const [collected, drag, dragPreview] = useDrag(
    {
      type: "box",
      item: { top: box.top, left: box.left }
    },
    [box]
  );
```

ドロップするコンポーネントに対しては、useDropというhooksを使う
```
  const [collectedProps, drop] = useDrop(
    () => ({
      accept: "box",
      drop(item: Box, monitor) {
        const delta = monitor.getDifferenceFromInitialOffset() as XYCoord;
        const left = Math.round(item.left + delta.x);
        const top = Math.round(item.top + delta.y);
        setBox({ top, left });
        return undefined;
      }
    }),
    []
  );
```

monitor.getDifferenceFromInitialOffset()で、ドラッグ前と後の位置情報の差分を取得して取得した差分を加算する

