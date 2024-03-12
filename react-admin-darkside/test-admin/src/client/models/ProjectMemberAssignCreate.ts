/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
export type ProjectMemberAssignCreate = {
    /**
     * プロジェクトID
     */
    project_id: number;
    /**
     * メンバーID
     */
    member_id: number;
    /**
     * コスト
     */
    cost: number;
    /**
     * 開始日
     */
    start_date: string;
    /**
     * 終了日
     */
    end_date?: (string | null);
};

