/* generated using openapi-typescript-codegen -- do no edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
export type ProjectBudget = {
    /**
     * プロジェクトID
     */
    project_id: number;
    /**
     * 開始日
     */
    start_date: string;
    /**
     * 終了日
     */
    end_date?: (string | null);
    /**
     * 予算
     */
    budget: number;
    id: number;
    created_at: string;
    deleted_at: (string | null);
};

