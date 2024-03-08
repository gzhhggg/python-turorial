import { fetchUtils } from "react-admin";

const apiUrl = "http://localhost:8000";
const httpClient = fetchUtils.fetchJson;

const dataProvider = {
  getList: async (resource, params) => {
    // React-Adminからのページネーションとソートのパラメータを取得
    const { page, perPage } = params.pagination;
    const { field, order } = params.sort;

    // FastAPIエンドポイントに渡すクエリパラメータを構築
    const query = {
      start: (page - 1) * perPage,
      end: page * perPage,
      sort: field,
      order: order,
    };

    const url = `${apiUrl}/${resource}?${new URLSearchParams(
      query
    ).toString()}`;

    // HTTPクライアントを使用してAPIからデータを取得
    const { headers, json } = await httpClient(url);

    // レスポンスヘッダから合計件数を取得
    const contentRange = headers.get("Content-Range");
    const total = contentRange
      ? parseInt(contentRange.split("/").pop(), 10)
      : json.length;

    return {
      data: json,
      total: total,
    };
  },

  // 他のメソッドも同様に実装
};

export default dataProvider;
